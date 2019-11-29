"""
THIS IS SPACY'S BERT MODEL THAT WE HAVE LOADED FOR OUR USE!

TRAIN DATA (JSON)
= [(
    {"id": int,                     # ID of the Conversation
    "dialogues": [{                 # list of dialogues in the corpus
        "id": int,                  # id of dialogue
        "raw": string,              # raw text of the paragraph
        "sentences": [{             # list of sentences in the paragraph
            "tokens": [{            # list of tokens in the sentence
                "id": int,          # index of the token in the document
                "dep": string,      # dependency label
                "head": int,        # offset of token head relative to token index
                "tag": string,      # part-of-speech tag
                "orth": string,     # verbatim text of the token
                "ner": string       # BILUO label, e.g. "O" or "B-ORG"
            }],
            "brackets": [{          # phrase structure (NOT USED by current models)
                "first": int,       # index of first token
                "last": int,        # index of last token
                "label": string     # phrase label
            }],
            "features": [{          # features for Dialogue Classifier
                "label": string,    # text feature label
                "value": float      # label value
            }]
        }],
        "speaker": int,             # speaker id
        "start": timestamp,         # start time
        "end": timestamp,           # end time
        "features": [{              # features for Dialogue Classifier
            "label": string,        # text feature label
            "value": float / bool   # label value
        }]
    }]},
    {
    "cats": {                       # cats for Call Classifier
        "label": value,             # text category value}
    }
)]
"""


import spacy
from spacy.util import minibatch
import random
import torch
import pandas as pd
from feature_engineering.bl.acts import *
from feature_engineering.bl.intents import *
from feature_engineering.bl.tags.SynTagsDialogueFeatureEngineerImpl import SynTagsDialogueFeatureEngineerImpl
from feature_engineering.bl.tags.AntoTagsDialogueFeatureEngineerImpl import AntoTagsDialogueFeatureEngineerImpl
from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent
from feature_engineering.bl.AbstractDialogueFeatureEngineerFactory import AbstractDialogueFeatureEngineerFactory

nlp = spacy.load('en_core_web_sm')

train_df = pd.read_csv('../data/altrain.csv', encoding='latin1')
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin1')

TRAIN_DATA = []

labels = [
            'Used_appropriate_opening_and_prepared_for_the_call',
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
            'Followed_all_relevant_policy_and_procedures_including_customer_verification_and_product_up_sells'
        ]

count = 0
for row in labels_df.values:
    if count == 3:
        break
    train_row = {}
    train_row['id'] = row[0]
    print('processing conversation id:', train_row['id'])
    train_row['dialogues'] = []
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    for val in rows.values:
        dialogues = {}
        dialogues['raw'] = val[4]
        dialogues['sentences'] = []
        doc = nlp(val[4])
        for sent in doc.sents:
            sents = {}
            sents['tokens'] = []
            for token in sent:
                tokens = {}
                tokens['id'] = token.idx
                tokens['dep'] = token.dep_
                tokens['head'] = token.head
                tokens['tag'] = token.tag_
                tokens['ner'] = token.ent_type_
                tokens['orth'] = token.orth
                tokens['synonyms'] = []
                synonyms = SynTagsDialogueFeatureEngineerImpl().synonyms(token)
                for syn in synonyms:
                    syn = nlp(syn)
                    for tok in syn:
                        tokens['synonyms'].append({'id': tok.orth})
                tokens['antonyms'] = []
                antonyms = AntoTagsDialogueFeatureEngineerImpl().antonyms(token)
                for ant in antonyms:
                    ant = nlp(ant)
                    for tok in ant:
                        tokens['antonyms'].append({'id': tok.orth})
                sents['tokens'].append(tokens)
            sents['brackets'] = []
            dialogues['sentences'].append(sents)
        dialogues['speaker'] = val[1]
        dialogues['start'] = val[2]
        dialogues['end'] = val[3]
        dialogues['WPM'] = val[15]
        dialogues['Hold'] = val[16]
        dialogues['DaleChalla'] = val[76]
        dialogues['FleschReading'] = val[77]
        dialogues['FoggIndex'] = val[78]
        dialogues['SmogIndex'] = val[79]
        k = 17
        for child in AbstractDialogueIntent().__class__.__subclasses__():
            dialogues[child.__name__[:-18]] = val[k]
            k += 1
        k = 80
        for child in AbstractDialogueAct().__class__.__subclasses__():
            dialogues[child.__name__[:-18]] = val[k]
            k += 1
        # SKIPPING CO-REFERENCE TAGS
        train_row['dialogues'].append(dialogues)

    cats = {}
    cats['cats'] = {}
    j = 0
    for i in range(14, 32):
        cats['cats'][labels[j]] = row[i]
        j += 1

    TRAIN_DATA.append((train_row, cats))
    count += 1


is_using_gpu = spacy.prefer_gpu()
if is_using_gpu:
    torch.set_default_tensor_type("torch.cuda.FloatTensor")

nlp = spacy.load("en_trf_bertbaseuncased_lg")
print(nlp.pipe_names)
textcat = nlp.create_pipe("trf_textcat", config={"exclusive_classes": True})
for label in labels:
    textcat.add_label(label)
nlp.add_pipe(textcat)

optimizer = nlp.resume_training()
for i in range(10):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for batch in minibatch(TRAIN_DATA, size=8):
        texts, cats = zip(*batch)
        nlp.update(texts, cats, sgd=optimizer, losses=losses)
    print(i, losses)
nlp.to_disk("/bertmodels")

