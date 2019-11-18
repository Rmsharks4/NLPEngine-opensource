from keras import backend as K
import keras.layers as layers
from keras.models import Model, load_model
from keras.engine import Layer
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import nltk
from nltk.corpus import wordnet


nlp = spacy.load('en_core_web_sm')

train_df = pd.read_csv('../data/altrain.csv', encoding='latin1')
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin1')

num_of_convs = labels_df['Call_Log'].count()
print('Number', num_of_convs)

features = ['SpeakerDataImpl', 'TokenTagsDialogueFeatureEngineerImpl', 'POSTagsDialogueFeatureEngineerImpl',
            'NounChunkTagsFeatureEngineerImpl', 'NERTagsDialogueFeatureEngineerImpl',
            'SynTagsDialogueFeatureEngineerImpl', 'AntoTagsDialogueFeatureEngineerImpl',
            'DepTagsDialogueFeatureEngineerImpl', 'SentTagsDialogueFeatureEngineerImpl',
            'IOBTagsDialogueFeatureEngineerImpl', 'CorefTagsDialogueFeatureEngineerImpl',
            'HoldTimeDialogueFeatureEngineerImpl', 'WordsPerMinuteDialogueFeatureEngineerImpl',
            'BackwardStepsDialogueFeatureEngineerImpl', 'QWhDialogueActImpl',
            'QYnDialogueActImpl', 'ForwardStepsDialogueFeatureEngineerImpl',
            'DaleChallaDifficultyIndexDialogueFeatureEngineerImpl']

final = list()
summ = 0
maxi = 0
train_data = []

for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    if len(rows) > maxi:
        maxi = len(rows)
    summ += len(rows)
    train_data.append([[row[1],   # SPEAKER
                        row[13],  # TOKENS
                        row[15],  # WPM
                        row[16],  # HOLD TIME
                        # row[67],  # ANTO
                        row[68],  # COREF
                        row[69],  # DEP
                        row[70],  # IOB
                        row[71],  # NER
                        row[72],  # NOUN
                        row[73],  # POS
                        row[74],  # SENT
                        # row[75],  # SYN
                        row[76],  # DALE CHALLA
                        row[81],  # QWH
                        row[82],  # QYN
                        row[83],  # BACK STEPS
                        row[84]   # FORW STEPS
                        ] for row in rows.values])

avg = summ / num_of_convs

print('Average', avg)
print('Maxximum', maxi)

# print(train_data)

input_shape = (num_of_convs, avg, len(features))
# input shape: 113, 46, 18

# Vectorize Data Now!

def numpy_fillna(data):
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    print('LENS')

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:, None]

    print('MASK')

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape, dtype=data.dtype)

    print('ZEROES')

    out[mask] = np.concatenate(data)

    print('CONCATENATE')

    return out


# data = np.asarray([np.pad(r, (0, maxi - len(r)), 'constant', constant_values=0) for r in train_data])

print('Conversations', np.array(train_data).shape)

for row in train_data:
    print('Dialogue', np.array(row).shape)
    for data in row:
        print('Features', data)
