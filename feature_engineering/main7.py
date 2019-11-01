
import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

df = pd.read_csv('../data/FeatureEngineeringService.csv', sep=',', encoding='utf-8')


def clean(data):
    doc = nlp(str(data))
    return [(token, token.tag_) for token in doc]
#
#
# for col in df.columns:
#     df[col].apply(lambda x: clean(x))
#
# df.to_csv('../data/AbstractDialoguePreProcessor.csv', sep=',', index=None)


from feature_engineering.bl.acts.ImpDialogueActImpl import ImpDialogueActImpl
from feature_engineering.bl.acts.QWhDialogueActImpl import QWhDialogueActImpl
from feature_engineering.bl.acts.QYnDialogueActImpl import QYnDialogueActImpl
from feature_engineering.utils.ActsUtils import ActsUtils


df['POSTagsDialogueFeatureEngineerImpl'] = df['RemovePunctuationDialoguePreProcessorImpl'].apply(lambda x: clean(x))

tststs = ActsUtils()
tststs.load()

df['QYnDialogueActImpl'] = QYnDialogueActImpl().engineer_feature_operation({
        'POSTagsDialogueFeatureEngineerImpl': df['POSTagsDialogueFeatureEngineerImpl'],
        'ActsUtils': tststs
    })

# print(df['ImpDialogueActImpl'])
