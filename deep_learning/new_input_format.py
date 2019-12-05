"""

-------------------------- DATA -------------------------------------

[conversation id:
    [dialogue id:
        [sentence id:
            [
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

import pandas as pd
from nltk.tokenize import word_tokenize
import spacy
import numpy as np
from nltk.corpus import stopwords
import nltk
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

stop_words = stopwords.words('english')
lemmatizer = nltk.stem.WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

train_df = pd.read_csv('../data/altrain.csv', encoding='latin1')
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin1')

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

dials = []
sentences = []

for row in train_df.values:
    dials.append(str(row[4]))
    doc = nlp(str(row[4]))
    for sent in doc.sents:
        sentences.append(sent.text)

convs = []

for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    call = ''
    for val in rows.values:
        call += str(val[4]) + ' '
    convs.append(call)


def clean(data):
    data = word_tokenize(data)
    data = [word for word in data if word.isalpha()]
    data = [w for w in data if not w in stop_words]
    data = [lemmatizer.lemmatize(w, pos='v') for w in data]
    return data


corpus = ' '.join(c for c in dials)
corpus = clean(corpus)
sentence_data = [TaggedDocument(words=clean(d), tags=[str(i)]) for i, d in enumerate(sentences)]
dialogue_data = [TaggedDocument(words=clean(d), tags=[str(i)]) for i, d in enumerate(dials)]
conversation_data = [TaggedDocument(words=clean(d), tags=[str(i)]) for i, d in enumerate(convs)]

print('making word model')
words_model = Word2Vec(corpus,
                 min_count=1,
                 size=200,
                 workers=2,
                 window=5,
                 iter=30)

print('making sentence model')
sent_model = Doc2Vec(sentence_data,
                 min_count=1,
                 size=200,
                 workers=2,
                 window=5,
                 iter=30)

print('making dialogue model')
dialogue_model = Doc2Vec(dialogue_data,
                 min_count=1,
                 size=200,
                 workers=2,
                 window=5,
                 iter=30)

print('making call model')
call_model = Doc2Vec(conversation_data,
                 min_count=1,
                 size=200,
                 workers=2,
                 window=5,
                 iter=30)
