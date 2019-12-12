"""

-------------------------- DATA -------------------------------------

[conversation id:
    [dialogue id:
        [sentence id:
            [ embedding:
                [id,
                first,
                last,
                dep,
                head,
                tag,
                orth,
                ner,
                synonyms: [id] x num_of_synonyms,
                antonyms: [id] x num_of_antonyms
            ] x num_of_words,
            [first, last, value] x num_of_chunks,
            [id, trace: [first, last] x num_of_traces] x num_of_corefs,
            [first, last, value] x num_of_acts,
            [first, last, value] x num_of_intents
        ] x num_of_sentences,
        speaker,
        feature_id: [val] x num_of_features] x num_of_dialogues
    ],
    cat_id: [val] x num_of_cats
]

"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import spacy
import numpy as np
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from flashtext.keyword import KeywordProcessor
import csv
import keras
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Input, Embedding, Concatenate
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

stop_words = stopwords.words('english')
lemmatizer = nltk.stem.WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

train_df = pd.read_csv('../data/train_corpus.csv', encoding='latin1')
labels_df = pd.read_csv('../data/train_labels.csv', encoding='latin1')

TRAIN_DATA = []

labels = ['Used_appropriate_opening_and_prepared_for_the_call',
          'Actively_listened_and_acknowledged_concerns',
          'Expressed_sincere_and_appropriate_Empathy',
          'Enthusiastic_and_Helpful_Tone',
          'Confidence_and_demonstrated_ownership',
          'Used_appropriate_closing',
          'Integrity_and_Professionalism',
          'Clear_and_easily_understood',
          'Used_appropriate_word_choices_or_phrasing',
          'Natural_use_of_customers_name_and_avoided_excessive_Sir_or_Maam',
          'Maintained_control_of_the_call',
          'Guided_the_call_towards_a_logical_resolution',
          'Utilized_tools_and_resources_efficiently',
          'Remained_focused_and_avoided_unexplained_dead_air',
          'Clear_and_concise_notations',
          'Reviewed_notes_or_history_and_probed_as_necessary',
          'Processed_the customers_request_and_with_accuracy',
          'Provided_correct_information_and_addressed_all_concerns',
          'Followed_all_relevant_policy_and_procedures_including_customer_verification_and_product_up_sells']

"""
BUILD FEATUIRES

---- 1. PER CONVERSATION ---------
- Contact_Reason (MUST WRITE CODE THAT CHECKS FOR THIS AND THEN INCLUDE THIS AS A FEATURE)
- Expressed_sincere_and_appropriate_Empathy
- Enthusiastic_and_Helpful_Tone
- Integrity_and_Professionalism
- Used_appropriate_word_choices_or_phrasing
- Remained_focused_and_avoided_unexplained_dead_air

---- 2. PER DIALOGUE -------------
- Speaker
- Hold Time

---- 3. PER SENTENCE -------------
- Acts: Qwh, QYn, Imp
- ForwardSteps
- Intents: accept, acknowledge, agree, bad_news, clear, compliment, good_news, guess, hesitate, interrupt, negate, offer, 
pardon, promise, refuse, sympathy, thank
- Tags: noun-chunks, coref (CURRENTLY IGNORING THIS UNTIL I COME UP WITH A MORE APPROPRIATE REPRESENTATION)

---- 4. PER WORD -----------------
- Tags: pos, ner, dep
"""


def clean(data):
    data = word_tokenize(data)
    data = [word for word in data if word.isalpha()]
    data = [w for w in data if not w in stop_words]
    data = [lemmatizer.lemmatize(w, pos='v') for w in data]
    if len(data) == 0:
        data = ['']
    return data


def imp_act(sent):
    for word in sent:
        if word.pos_ == 'VB':
            return 1
        else:
            return 0


def qwh_act(sent):
    for word in sent:
        if word.pos_ == 'WDT' or word.pos_ == 'WP' or word.pos_ == 'WP$' or word.pos_ == 'WRB':
            return 1
    return 0


def qyn_act(sent):
    for word in sent:
        if word.pos_ == 'MD':
            return 1
        else:
            return 0


def get_kp(file):
    kp = KeywordProcessor()
    with open('../data/intents/' + file + '.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for read in reader:
            kp.add_keyword(read[0], read[1])
    return kp


def accept(sent):
    kp = get_kp('AcceptDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def acknowledge(sent):
    kp = get_kp('AcknowledgeDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def agree(sent):
    kp = get_kp('AgreeDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def badnews(sent):
    kp = get_kp('BadNewsDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def clear(sent):
    kp = get_kp('ClearDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def compliment(sent):
    kp = get_kp('ComplimentDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def goodnews(sent):
    kp = get_kp('GoodNewsDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def guess(sent):
    kp = get_kp('GuessDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def hesitate(sent):
    kp = get_kp('HesitateDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def interrupt(sent):
    kp = get_kp('InterruptDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def negate(sent):
    kp = get_kp('NegateDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def offer(sent):
    kp = get_kp('OfferDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def pardon(sent):
    kp = get_kp('PardonDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def promise(sent):
    kp = get_kp('PromiseDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def refuse(sent):
    kp = get_kp('RefuseDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def sympathy(sent):
    kp = get_kp('SympathyDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


def thank(sent):
    kp = get_kp('ThankDialogueIntentImpl')
    if len(kp.extract_keywords(sent)) > 0:
        return 1
    return 0


convs = []
conv_features = []

train_dials = []
dials = []
dial_features = []

train_words = []
word_features = []
total_word_features = []
corpus = []

max_words = []
max_dials = []

# Drop Sentences for now! - theyre one and the same!

print('Iterating Calls: Preprocessing and Feature Engineering')

for row in labels_df.values:
    conv_features.append([row[16], row[17], row[20], row[22], row[27]])
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    max_dials.append(len(rows))
    call = ''
    call_dials = []
    call_dial_feats = []
    call_words = []
    call_word_feats = []
    for val in rows.values:
        dial = str(val[4]).strip().lower()
        call += dial + ' '
        call_dials.append(dial)
        doc = nlp(str(val[4]).strip().lower())
        call_dial_feats.append([val[1], val[16], imp_act(doc), qwh_act(doc), qyn_act(doc), accept(dial),
                                acknowledge(dial), agree(dial), badnews(dial), clear(dial), compliment(dial),
                                goodnews(dial), guess(dial), hesitate(dial), interrupt(dial), negate(dial), offer(dial),
                                pardon(dial), promise(dial), refuse(dial), sympathy(dial), thank(dial)])
        words = clean(str(dial).strip().lower())
        max_words.append(len(words))
        cleaned = nlp(' '.join(c for c in words))
        dial_words = []
        dial_word_feats = []
        for word in cleaned:
            dial_words.append(word.text)
            word_feat = [word.pos_, word.ent_type_, word.dep_]
            dial_word_feats.append(word_feat)
            total_word_features.append(word_feat)
        train_words.extend(dial_words)
        call_words.append(dial_words)
        call_word_feats.append(dial_word_feats)
    train_dials.extend(call_dials)
    corpus.append(call_words)
    word_features.append(call_word_feats)
    dials.append(call_dials)
    dial_features.append(call_dial_feats)
    convs.append(call)

print('Vectorization:')

dialogue_data = [TaggedDocument(words=clean(d), tags=[str(i)]) for i, d in enumerate(train_dials)]
conversation_data = [TaggedDocument(words=clean(d), tags=[str(i)]) for i, d in enumerate(convs)]

print('making word model:')
words_model = Word2Vec([train_words],
                       min_count=1,
                       size=200,
                       workers=2,
                       window=5,
                       iter=30)

print('making dialogue model:')
dialogue_model = Doc2Vec(min_count=1,
                         vector_size=200,
                         workers=2,
                         window=5,
                         epcohs=30)
dialogue_model.build_vocab(dialogue_data)
dialogue_model.train(dialogue_data,
                     total_examples=dialogue_model.corpus_count,
                     epochs=dialogue_model.epochs)

print('making call model:')
call_model = Doc2Vec(min_count=1,
                     vector_size=200,
                     workers=2,
                     window=5,
                     epochs=30)
call_model.build_vocab(conversation_data)
call_model.train(conversation_data,
                 total_examples=call_model.corpus_count,
                 epochs=call_model.epochs)

print('Padding Sequences:')

conv_embeddings = []
for data in convs:
    emb = call_model.infer_vector(clean(data))
    conv_embeddings.append(emb)

max_dial_length = max(n.shape for n in np.array(train_dials))
max_sent_length = 0

dial_embeddings = []
for data in dials:
    dial_emb = []
    for dialogue in data:
        emb = dialogue_model.infer_vector(clean(dialogue))
        dial_emb.append(emb)
    dial_embeddings.append(dial_emb)

dial_embeddings = pad_sequences(dial_embeddings)

word_embeddings = []
for data in corpus:
    dial_emb = []
    for dialogue in data:
        word_emb = []
        for word in dialogue:
            emb = words_model.wv[word]
            word_emb.append(emb)
        if len(dialogue) == 0:
            word_emb.append(np.zeros(shape=(200,)))
        dial_emb.append(word_emb)
    dial_emb = pad_sequences(dial_emb, maxlen=max(max_words))
    word_embeddings.append(dial_emb)

word_embeddings = pad_sequences(word_embeddings)

print('Conv Embeddings')
print('Shape', np.array(conv_embeddings).shape)

print('Dial Embeddings')
print('Shape', np.array(dial_embeddings).shape)

print('Word Embeddings')
print('Shape', np.array(word_embeddings).shape)

"""
# CONVERSATION FEATURES: ONE-HOT

# BINNING
# DIALOGUE FEATURES: SPEAKER BINS (CALLER, CSR, OTHER) AND HOLD TIME BINS (IGNORE, MUTE, SOFT, HARD, FATAL)

# SENTENCE FEATURES: ONE-HOT

# BINNING
# WORD FEATURES: POS, NER AND DEP - AUTO BINNING!
"""

print('Binning Features:')
binned_dial_features = []
for dial in dial_features:
    dial_feats = []
    for fea in dial:
        if fea[0] == 0:
            speaker = [1, 0, 0]
        elif fea[0] == 1:
            speaker = [0, 1, 0]
        else:
            speaker = [0, 0, 1]
        if fea[1] < 2:
            hold = [1, 0, 0, 0, 0]
        elif fea[1] < 4:
            hold = [0, 1, 0, 0, 0]
        elif fea[1] < 9:
            hold = [0, 0, 1, 0, 0]
        elif fea[1] < 241:
            hold = [0, 0, 0, 1, 0]
        else:
            hold = [0, 0, 0, 0, 1]
        total = []
        total.extend(speaker)
        total.extend(hold)
        dial_feats.append(total)
    binned_dial_features.append(dial_feats)

binned_dial_features = pad_sequences(binned_dial_features)

enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(total_word_features)

binned_word_features = []
for data in word_features:
    dial_feat = []
    for dialogue in data:
        word_feat = []
        for word in dialogue:
            feat = enc.transform([word]).toarray().flatten()
            word_feat.append(feat)
        if len(dialogue) == 0:
            word_feat.append(np.zeros(shape=(75, )))
        dial_feat.append(word_feat)
    dial_feat = pad_sequences(dial_feat, maxlen=max(max_words))
    binned_word_features.append(dial_feat)

binned_word_features = pad_sequences(binned_word_features)

print('Conv Features')
print('Shape', np.array(conv_features).shape)

print('Dial Features')
print('Shape', np.array(binned_dial_features).shape)

print('Word Features')
print('Shape', np.array(binned_word_features).shape)

"""
BUILD MODEL
0. Sequential
1. CNN
2. DNN
3. RNN
4. BRNN
5. LSTM
6. GRU
"""

seq_model = Sequential()
cnn_model = None
dnn_model = None
rnn_model = None
bi_rnn_model = None
lstm_model = None
gru_model = None

"""
model structure - every time:
- conv_emb + conv_features (3rd dimension)
- dial_emb + dial_features (3rd dimension) x num_of_dialogues (pad this!)
- sent_emb + sent_features (3rd dimension) x num_of_sentences (pad this!)
- word_emb + word_features (2nd dimension) x num_of_words (pad this!)
"""

call_emb_layer = Sequential()
call_emb_layer.add(Embedding(input_length=1, input_dim=(200, )))

call_feat_layer = Sequential()
call_feat_layer.add(Input(shape=(5, )))

merge_call_layer = Sequential()
merge_call_layer.add(Concatenate([call_emb_layer, call_feat_layer]))

dial_emb_layer = Sequential()
dial_emb_layer.add(Embedding(input_length=1, input_dim=(193, 200)))

dial_feat_layer = Sequential()
dial_feat_layer.add(Input(shape=(193, 8)))

merge_dial_layer = Sequential()
merge_dial_layer.add(Concatenate([dial_emb_layer, dial_feat_layer]))

word_emb_layer = Sequential()
word_emb_layer.add(Embedding(input_length=1, input_dim=(193, 222, 200)))

word_feat_layer = Sequential()
word_feat_layer.add(Input(shape=(193, 222, 75)))

merge_word_layer = Sequential()
merge_word_layer.add(Concatenate([word_emb_layer, word_feat_layer]))

