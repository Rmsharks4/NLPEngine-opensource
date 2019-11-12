
import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

df = pd.read_csv('../../data/FeatureEngineeringService.csv', sep=',', encoding='utf-8')


def clean(data):
    doc = nlp(str(data))
    return [(token, token.tag_) for token in doc]


from feature_engineering.bl.steps.ForwardStepsDialogueFeatureEngineerImpl import ForwardStepsDialogueFeatureEngineerImpl
from feature_engineering.bl.steps.BackwardStepsDialogueFeatureEngineerImpl import BackwardStepsDialogueFeatureEngineerImpl
from feature_engineering.bl.intents import *
from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent
from feature_engineering.utils.KeyProcessor import KeyProcessor
from feature_engineering.utils.ActsUtils import ActsUtils


# df['POSTagsDialogueFeatureEngineerImpl'] = df['RemovePunctuationDialoguePreProcessorImpl'].apply(lambda x: clean(x))

tststs = KeyProcessor()
tststs.load()

abs = AbstractDialogueIntent()

args = dict()

for child in abs.__class__.__subclasses__():
    df[child.__name__] = child().engineer_feature_operation({
        'RemovePunctuationDialoguePreProcessorImpl': df['RemovePunctuationDialoguePreProcessorImpl'],
        'KeyProcessor': tststs
    })
    args[child.__name__] = df[child.__name__]

tststs = ActsUtils()
tststs.load()

args['ActsUtils'] = tststs

df['BackwardStepsDialogueFeatureEngineerImpl'] = BackwardStepsDialogueFeatureEngineerImpl().engineer_feature_operation(args)

print(df['BackwardStepsDialogueFeatureEngineerImpl'])
