import os
import pandas as pd
from flashtext.keyword import KeywordProcessor
import csv
import re
import numpy as np
import spacy
nlp = spacy.load('en_core_web_sm')

dir_str = '../data/intents/'

directory = os.fsencode(dir_str)

df = pd.read_csv('../data/AbstractDialoguePreProcessor.csv', sep=',', encoding='utf-8')

output = pd.DataFrame({'Call_ID': df['Call_ID'],
                       'Speaker': df['Speaker'],
                       'Dialogue': df['SpellCheckerDialoguePreProcessorImpl'].dropna()
                       })
output = output.dropna()


def get_intents():
    kps = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        kp = KeywordProcessor()
        with open(dir_str+filename, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                kp.add_keyword(row[0], row[1])
        kps.append(kp)
        print(filename[:-4])
    return kps


keyps = get_intents()
output['Dialogue'] = output['Dialogue'].apply(lambda x: re.sub('(\s){2,}',' ', x))
output['Dialogue'] = output['Dialogue'].apply(lambda x: x.strip())
output['Dialogue'].replace('', np.nan, inplace=True)
output = output.dropna(subset=['Dialogue'])


def get_ints(row):
    intents = []
    for kp in keyps:
        res = [str(k) for k in kp.extract_keywords(str(row))]
        if len(res) > 0:
            for r in res:
                intents.append(r)
    return intents


output['Intents'] = output['Dialogue'].apply(lambda x: ', '.join(ints for ints in get_ints(x)))
output['Ents'] = df['SpellCheckerDialoguePreProcessorImpl.PlainTextDialoguePreProcessorImpl'].dropna().apply(lambda x: ','.join('('+str(y)+', '+str(y.label_)+')' for y in nlp(str(x)).ents))
output.to_csv('Intents.csv', index=None)
