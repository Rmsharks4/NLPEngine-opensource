import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import spacy
import numpy as np
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from flashtext.keyword import KeywordProcessor
import csv
import keras
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Input, Embedding, Concatenate
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

stop_words = stopwords.words('english')
lemmatizer = nltk.stem.WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

train_df = pd.read_csv('../data/train_corpus.csv', encoding='latin1')
labels_df = pd.read_csv('../data/train_labels.csv', encoding='latin1')

call_ids = labels_df['Call_Log'].unique()

binned_speaker = []
binned_hold_time = []
dialogue_corpus = []

for id in call_ids:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == str(id))
    rows = rows.dropna()
    speaker_ids = np.sort(rows['SpeakerDataImpl'].unique())
    for dialogue in rows:
        if dialogue[1] == speaker_ids[0]:
            binned_speaker.append('CSR')
        else:
            binned_speaker.append('Caller')
        if dialogue[16] < 2:
            binned_hold_time.append('Normal')
        elif dialogue[16] < 4:
            binned_hold_time.append('Mute')
        elif dialogue[6] < 9:
            binned_hold_time.append('Soft')
        elif dialogue[16] < 241:
            binned_hold_time.append('Hard')
        else:
            binned_hold_time.append('Fatal')
        dialogue_corpus.append(str(dialogue[4]))

labels = labels_df['Actively_listened_and_acknowledged_concerns'].values

train_df['bineed_speaker'] = binned_speaker
train_df['binned_hold_time'] = binned_hold_time

train_rows = []

for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == str(row[0]))
    rows = rows.dropna()
    call_entry = []
    prev = 0
    next = 0
    for dialogue in rows:
        next += 1
        if dialogue[85] == 'CSR':
            index = dialogue[2]
            entry = []

            dial_emb = str(dialogue[4])
            acknowledge_feats = [dialogue[18], dialogue[19], dialogue[21], dialogue[48], dialogue[52], dialogue[58],
                                 dialogue[63], dialogue[64]]
            """
            Acknowledgement Features:
            accept, acknowledge, agree, negate, pardon, refuse, sympathy, thank
            """
            concern_feats = [dialogue[26], dialogue[30], dialogue[38], dialogue[41], dialogue[44], dialogue[50]]
            """
            Concern Features:
            clear, confirm, guess, indifference, interrupt, offer help 
            """
            attentive_feats = [dialogue[39], dialogue[40], dialogue[59], dialogue[86]]
            """
            Attentive Features:
            hesitate, hold, repeat, HOLD_TIME
            """

            caller_context = []
            caller_rows = rows[prev:next]
            caller_dialogues = ' '.join([str(dial[4]) for dial in caller_rows.where(
                caller_rows['binned_speaker'] == 'Caller')])
            for ctx in caller_rows.where(caller_rows['binned_speaker'] == 'Caller'):
                query_feats = [ctx[31], ctx[32], ctx[54], ctx[60], ctx[67], ctx[82], ctx[83]]
                """
                Query Features:
                demand, desire, preference, request, wish, QWH, QYN
                """
                unsatisfied_feats = [ctx[26], ctx[27], ctx[28], ctx[33], ctx[59], ctx[64]]
                """
                Unsatisfied Features:
                clear, complaint, compliment, disappoint, repeat, thank
                """

            entry.append(caller_context)
            call_entry.append(entry)
            prev = next

    train_rows.append([call_entry, row[16], row[17], row[20], row[22], row[27]])


def clean(data):
    data = word_tokenize(data)
    data = [word for word in data if word.isalpha()]
    data = [w for w in data if not w in stop_words]
    data = [lemmatizer.lemmatize(w, pos='v') for w in data]
    if len(data) == 0:
        data = ['']
    return data

