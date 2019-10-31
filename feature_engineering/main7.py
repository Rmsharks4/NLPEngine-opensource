
import pandas as pd

df = pd.read_csv('../data/FeatureEngineeringService.csv', sep=',', encoding='utf-8')

cols = ['SpellCheckerDialoguePreProcessorImpl', 'SpellCheckerDialoguePreProcessorImpl.PlainTextDialoguePreProcessorImpl']

strname = 'SpellCheckerDialoguePreProcessorImpl'


def trim(col):
    ngs = zip(*[col[i:] for i in range(3)])
    print([','.join(ngram for ngram in ngs)])


df[cols].apply(lambda x: x.apply(lambda y: trim(y)) if x.name == strname else None)
