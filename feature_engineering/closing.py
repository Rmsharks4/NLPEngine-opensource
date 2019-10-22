import pandas as pd
import spacy
import neuralcoref
from flashtext.keyword import KeywordProcessor
import csv
import re

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)


def sents(args):
    doc = nlp(args)
    return [sent for sent in doc.sents]


def chunks(args):
    doc = nlp(args)
    return [chunk for chunk in doc.noun_chunks]


def corefs(args):
    doc = nlp(args)
    return [coref for coref in doc._.coref_clusters]


def tags(args):
    doc = nlp(args)
    return [(re.sub("\s\s+", " ", token.text), re.sub("\s\s+", " ", token.lemma_), token.pos_, token.ent_type_, token.dep_) for token in doc]


def person(args):
    doc = nlp(args)
    return [ee for ee in doc.ents if ee.label_ == 'PERSON']


def org(args):
    doc = nlp(args)
    return [ee for ee in doc.ents if ee.label_ == 'ORG']


# APPROPRIATE OPENING DATASET
# CONVERSATION[0:4], GREET{2], INTRODUCE_SELF[2], INTRODUCE_COMPANY[2], OFFER[2]

by = KeywordProcessor()

with open('../data/intents/ByeDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        by.add_keyword(row[0])

co = KeywordProcessor()

with open('../data/intents/IntroduceCompanyDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        co.add_keyword(row[0])

th = KeywordProcessor()

with open('../data/intents/ThankDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        th.add_keyword(row[0])

of = KeywordProcessor()

with open('../data/intents/OfferDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        of.add_keyword(row[0])

df = pd.read_csv('../data/AbstractDialoguePreProcessor.csv', sep=',', encoding='utf-8')

output = None

for cid in df['Call_ID'].unique():
    if cid == 1:
        output = pd.DataFrame({'Call_ID': df['Call_ID'],
                               'Speaker': df['Speaker'],
                               'Dialogue': df['RemoveEmailsDialoguePreProcessorImpl.PlainTextDialoguePreProcessorImpl'].
                              where(df['Call_ID'] == cid)})
        output = output.dropna()
        output = output[-6:]
    else:
        temp = pd.DataFrame({'Call_ID': df['Call_ID'],
                             'Speaker': df['Speaker'],
                             'Dialogue': df['RemoveEmailsDialoguePreProcessorImpl.PlainTextDialoguePreProcessorImpl'].
                            where(df['Call_ID'] == cid)})
        temp = temp.dropna()
        output = output.append(temp[-6:], ignore_index=True)

output['Sentences'] = output['Dialogue'].apply(lambda x: ','.join(str(s) for s in sents(str(x))))
output['NounChunks'] = output['Dialogue'].apply(lambda x: ','.join(str(c) for c in chunks(str(x))))
output['Co-Reference'] = output['Dialogue'].apply(lambda x: ','.join(str(c) for c in corefs(str(x))))
output['Tags'] = output['Dialogue'].apply(lambda x: tags(str(x)))
output['PERSON'] = output['Dialogue'].apply(lambda x: ','.join(str(p) for p in person(str(x))))
output['ORG'] = output['Dialogue'].apply(lambda x: ','.join(str(o) for o in org(str(x))))

output['Bye'] = output['Dialogue'].apply(lambda x: ','.join(str(g) for g in by.extract_keywords(str(x))))

output['IntroduceCompany'] = output['Dialogue'].apply(lambda x: ','.join(str(c) for c in co.extract_keywords(str(x))))

output['Thank'] = output['Dialogue'].apply(lambda x: ','.join(str(o) for o in th.extract_keywords(str(x))))

output['Offer'] = output['Dialogue'].apply(lambda x: ','.join(str(o) for o in of.extract_keywords(str(x))))

output.to_csv('AppropriateClosing.csv', index=None)
