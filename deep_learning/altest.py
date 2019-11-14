from keras import backend as K
import keras.layers as layers
from keras.models import Model, load_model
from keras.engine import Layer
import pandas as pd
import numpy as np

train_df = pd.read_csv('../data/altrain.csv')
labels_df = pd.read_csv('../data/allabels.csv')

train_text = train_df['PlainTextDataImpl'].tolist()
train_text = [' '.join(t.split()[0:150]) for t in train_text]
train_text = np.array(train_text, dtype=object)[:, np.newaxis]
train_label = train_df['Actively_listened_and_acknowledged_concerns'].tolist()

input_text = layers.Input(shape=(1,), dtype="string")
embedding = layers.Embedding()(input_text)
dense = layers.Dense(256, activation='relu')(embedding)
pred = layers.Dense(1, activation='sigmoid')(dense)

model = Model(inputs=[input_text], outputs=pred)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(train_text,
          train_label,
          epochs=1,
          batch_size=32)

# https://github.com/strongio/keras-elmo/blob/master/Elmo%20Keras.ipynb
