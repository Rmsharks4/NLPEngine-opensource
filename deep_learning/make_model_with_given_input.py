"""

THIS IS SPACY'S BERT MODEL THAT WE HAVE LOADED FOR OUR USE!

TRAIN DATA (JSON)
= [{
    "id": int,                      # ID of the Conversation
    "raw": text,
    "dialogues": [{                 # list of dialogues in the corpus
        "sentences": [{             # list of sentences in the paragraph
            "first": int,
            "last": int,
            "tokens": [{            # list of tokens and tags in the sentence
                "id": int,          # index of the token in the document
                "first": int,
                "last": int,
                "dep": string,      # dependency label
                "head": int,        # offset of token head relative to token index
                "tag": string,      # part-of-speech tag
                "orth": string,     # verbatim text of the token
                "ner": string,       # BILUO label, e.g. "O" or "B-ORG"
                "synonyms": [],
                "antonyms": [],
            }],
            "chunks": [{
                "first": int,
                "last": int,
                "value": string          # Value
            }],
            "coref": [{
                "id": int,     # Coref token id
                "values": [{
                    first: int,
                    last: int
                }]
            }],
            "acts": [{
                "label": string,     # Act
                "first": int,
                "last": int,
                "value": []          # Value
            }],
            "intents": [{
                "label": string,     # Intent
                "first": int,
                "last": int,
                "value": []          # Value
            }]
        }],
        "speaker": int,             # speaker id
        "features": [{              # features for Dialogue Classifier
            "label": string,        # text feature label: WPM, Hold, Difficulty Index
            "value": float / bool   # label value
        }],
        "first": int,
        "last": int
    }],
    "cats": [{                      # cats for Call Classifier
        "label": string,            # text category label
        "value": float / bool       # label applies (1.0/true) or not (0.0/false)
    }]
}]

"""


import spacy
import pandas as pd
import numpy as np
from random import seed
from random import randint

seed(1)

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

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(min_df=0, lowercase=False)
corpus = []

for row in train_df.values:
    corpus.append(str(row[4]))

cv.fit(corpus)

count = 0
VECTORS = []

for row in labels_df.values:
    if count == 10:
        break
    vector = []
    conversation = dict()
    conversation['id'] = int(row[0])
    print('processing conversation: ', conversation['id'])
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    conv_text = []
    for val in rows.values:
        conv_text.append(str(val[4]))
    conversation['raw'] = '\n'.join(c for c in conv_text)
    vector.append(cv.transform(conv_text).toarray())
    conversation['dialogues'] = []
    dial_len = 0
    for val in rows.values:
        dialogue = dict()
        doc = nlp(val[4])
        dialogue['first'] = dial_len
        dial_len += len(str(val[4]))
        dialogue['last'] = dial_len
        dial_len += 1
        dialogue['speaker'] = val[1]
        dialogue['sentences'] = []
        for sent in doc.sents:
            sentence = dict()
            sentence['first'] = sent.start
            sentence['last'] = sent.end
            sentence['tokens'] = []
            for tok in sent:
                token = dict()
                token['first'] = tok.offset
                token['last'] = tok.offset + len(tok)
                token['id'] = tok.idx
                token['dep'] = tok.dep_
                token['head'] = tok.head_
                token['tag'] = tok.tag_
                token['ner'] = tok.ent_type_
                token['orth'] = tok.orth
                token['synonyms'] = [str(i) for i in range(randint(2, 10))]  # RANDOM REPLACE LATER
                token['antonyms'] = [str(i) for i in range(randint(2, 10))]  # RANDOM REPLACE LATER
                sentence['tokens'].append(np.array(list(token.items())))
            sentence['chunks'] = []  # RANDOM REPLACE LATER
            num_of_chunks = randint(2, 10)  # RANDOM REPLACE LATER
            for i in range(num_of_chunks):  # RANDOM REPLACE LATER
                chunk = dict()  # RANDOM REPLACE LATER
                chunk['first'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                chunk['last'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                chunk['value'] = str(randint(2, 10))  # RANDOM REPLACE LATER
                # CATEGORICAL DATA
                sentence['chunks'].append(np.array(list(chunk.items())))
            sentence['corefs'] = []  # RANDOM REPLACE LATER
            num_of_corefs = randint(2, 10)  # RANDOM REPLACE LATER
            for i in range(num_of_corefs):  # RANDOM REPLACE LATER
                coref = dict()  # RANDOM REPLACE LATER
                coref['id'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                coref['values'] = []  # RANDOM REPLACE LATER
                num_of_vals = randint(2, 10)  # RANDOM REPLACE LATER
                for j in range(num_of_vals):  # RANDOM REPLACE LATER
                    vals = dict()
                    vals['first'] = randint(2, 10)
                    # NUMERICAL DATA
                    vals['last'] = randint(2, 10)
                    # NUMERICAL DATA
                    coref['values'].append(np.array(list(vals.items())))
                sentence['corefs'].append(np.array(list(coref.items())))
            sentence['acts'] = []  # RANDOM REPLACE LATER
            num_of_acts = randint(2, 10)  # RANDOM REPLACE LATER
            for i in range(num_of_acts):  # RANDOM REPLACE LATER
                act = dict()  # RANDOM REPLACE LATER
                act['label'] = str(randint(2, 10))
                # CATEGORICAL DATA
                act['first'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                act['last'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                act['value'] = str(randint(2, 10))  # RANDOM REPLACE LATER
                # CATEGORICAL DATA
                sentence['acts'].append(np.array(list(act.items())))
            sentence['intents'] = []  # RANDOM REPLACE LATER
            num_of_intents = randint(2, 10)  # RANDOM REPLACE LATER
            for i in range(num_of_intents):  # RANDOM REPLACE LATER
                intent = dict()  # RANDOM REPLACE LATER
                intent['label'] = str(randint(2, 10))
                # CATEGORICAL DATA
                intent['first'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                intent['last'] = randint(2, 10)  # RANDOM REPLACE LATER
                # NUMERICAL DATA
                intent['value'] = str(randint(2, 10))  # RANDOM REPLACE LATER
                # CATEGORICAL DATA
                sentence['acts'].append(np.array(list(intent.items())))
            dialogue['sentences'].append(np.array(list(sentence.items())))
        dialogue['features'] = []  # RANDOM REPLACE LATER
        num_of_features = randint(2, 10)  # RANDOM REPLACE LATER
        for i in range(num_of_features):  # RANDOM REPLACE LATER
            feature = dict()  # RANDOM REPLACE LATER
            feature['label'] = str(randint(2, 10))
            # CATEGORICAL DATA
            feature['value'] = randint(2, 10)  # RANDOM REPLACE LATER
            # NUMERICAL DATA
            dialogue['features'].append(np.array(list(feature.items())))
        conversation['dialogues'].append(np.array(list(dialogue.items())))
    conversation['cats'] = []  # RANDOM REPLACE LATER

    j = 0
    for i in range(14, 32):
        cat = dict()
        cat['label'] = labels[j]
        cat['value'] = dict()
        if row[i]:
            cat['value']['POSITIVE'] = 1
            cat['value']['NEGATIVE'] = 0
        else:
            cat['value']['POSITIVE'] = 0
            cat['value']['NEGATIVE'] = 1
        j += 1
        conversation['cats'].append(np.array(list(cat.items())))
        vector.append(np.array([val for val in cat['value'].values()], dtype=int))
    VECTORS.append(vector)
    TRAIN_DATA.append(np.array(list(conversation.items())))
    count += 1

# print(np.array(VECTORS))

"""
MODEL IMPLEMENTATIONS GO HERE:
"""



