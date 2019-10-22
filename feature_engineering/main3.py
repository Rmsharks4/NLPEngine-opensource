import csv
import pandas as pd

# APPROPRIATE OPENING DATASET
# CONVERSATION[0:4], GREET{2], INTRODUCE_SELF[2], INTRODUCE_COMPANY[2], OFFER[2]

from flashtext.keyword import KeywordProcessor
import csv

gr = KeywordProcessor()

with open('../data/intents/GreetDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        gr.add_keyword(row[0])

se = KeywordProcessor()

with open('../data/intents/IntroduceSelfDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        se.add_keyword(row[0])

co = KeywordProcessor()

with open('../data/intents/IntroduceCompanyDialogueIntentImpl.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        co.add_keyword(row[0])

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
                               'Data': df['WordNetLemmatizerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl'].
                              where(df['Call_ID'] == cid)})
        output = output.dropna()
        output = output[:4]
    else:
        temp = pd.DataFrame({'Call_ID': df['Call_ID'],
                             'Speaker': df['Speaker'],
                             'Data': df['WordNetLemmatizerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl'].
                            where(df['Call_ID'] == cid)})
        temp = temp.dropna()
        output = output.append(temp[:4], ignore_index=True)

output['Greet'] = output['Data'].apply(lambda x: gr.extract_keywords(str(x)))

output['IntroduceSelf'] = output['Data'].apply(lambda x: se.extract_keywords(str(x)))

output['IntroduceCompany'] = output['Data'].apply(lambda x: co.extract_keywords(str(x)))

output['Offer'] = output['Data'].apply(lambda x: of.extract_keywords(str(x)))

print(output)
