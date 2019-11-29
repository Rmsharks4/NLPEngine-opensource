"""
THIS IS SPACY'S BERT MODEL THAT WE HAVE LOADED FOR OUR USE!

TRAIN DATA (JSON)
= [(
    "text",                 # Text of a Dialogue (CSR)
    "context",              # All Previous Text in Convo
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
    if count == 70:
        break
    text = None
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    context = ''
    for val in rows.values:
        text = val[4]
        cats = {}
        cats['cats'] = {}
        if row[15] == 0:
            cats['POSITIVE'] = 0
            cats['NEGATIVE'] = 1
        else:
            cats['POSITIVE'] = 1
            cats['NEGATIVE'] = 0
        TRAIN_DATA.append((text, context, cats))
        context += text
    count += 1

is_using_gpu = spacy.prefer_gpu()
if is_using_gpu:
    torch.set_default_tensor_type("torch.cuda.FloatTensor")

nlp = spacy.load("en_trf_bertbaseuncased_lg")
textcat = nlp.create_pipe("trf_textcat", config={"exclusive_classes": True})
for label in labels:
    textcat.add_label(label)
nlp.add_pipe(textcat)

optimizer = nlp.resume_training()
for i in range(1):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for batch in minibatch(TRAIN_DATA, size=8):
        texts, contexts, cats = zip(*batch)
        nlp.update(contexts+texts, cats, sgd=optimizer, losses=losses)
    print(i, losses)
nlp.to_disk("/bertmodels")

test = ('Hello \n', 'yes?')
text, context = zip(*test)
print(nlp(text+context))
