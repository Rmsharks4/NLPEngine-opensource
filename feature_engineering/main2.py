
import pandas as pd


df = pd.read_csv('../../data/Call_Transcripts.csv')
print(df.columns)

for dialogue in df['Call_ID'].unique():
    xml = ['<?xml version="1.0"?>']
    xml.append('<dialogue lang="en" id="'+str(dialogue)+'" corpus="train-data">')
    n = 1
    for index, turn in df.loc[df['Call_ID'] == dialogue].iterrows():
        xml.append('<turn speaker="'+str(turn['Speaker'])+'" n="'+str(n)+'">')
        text = ''
        for char in str(turn['Conversation']):
            if char is '.':
                xml.append(text)
                xml.append('<punct type="stop"/>')
                text = ''
            elif char is '?':
                xml.append(text)
                xml.append('<punct type="query"/>')
                text = ''
            else:
                text = text + char
        xml.append(text)
        xml.append('</turn>')
        n += 1
    xml.append('</dialogue>')
    xml_str = '\n'.join(xml)
    with open('data/train-data'+str(dialogue)+'.xml', 'w') as f:
        f.write(xml_str)

