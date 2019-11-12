
import spacy
import pandas as pd
import numpy
import csv
import string
from spacy import displacy
from spacy.attrs import ENT_IOB, ENT_TYPE
nlp = spacy.load('en_core_web_sm')

texts = 'Welcome to Australia Post Load and Go Support my name is Archie may I please have your card number.'

doc = nlp(texts)

print(string.punctuation)
print(doc.ents)

header = [ENT_IOB, ENT_TYPE]

with open('../../data/ORG.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        attr_array = [row[0], row[1]]

doc.from_array(header, numpy.asarray(attr_array))
print(doc.ents)
