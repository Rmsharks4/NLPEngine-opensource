from keras import backend as K
import keras.layers as layers
from keras.models import Model, load_model
from keras.engine import Layer
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


class ElmoEmbeddingLayer(Layer):
    def __init__(self, **kwargs):
        self.dimensions = 1024
        self.trainable = True
        self.elmo = None
        super(ElmoEmbeddingLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.elmo = hub.Module('https://tfhub.dev/google/elmo/2', trainable=self.trainable,
                               name="{}_module".format(self.name))

        self.trainable_weights += K.tf.trainable_variables(scope="^{}_module/.*".format(self.name))
        super(ElmoEmbeddingLayer, self).build(input_shape)

    def call(self, x, mask=None):
        result = self.elmo(K.squeeze(K.cast(x, tf.string), axis=1),
                           as_dict=True,
                           signature='default',
                           )['default']
        return result

    def compute_mask(self, inputs, mask=None):
        return K.not_equal(inputs, '--PAD--')

    def compute_output_shape(self, input_shape):
        return input_shape[0], self.dimensions


train_df = pd.read_csv('../data/altrain.csv', encoding='latin1')
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin1')

final = list()

for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    # vals = list()
    # for val in rows.values:
    #     vals.append([val[1], val[4]])
    # final.append([row[0], vals, row[15]])
    for val in rows.values:
        if row[15] == 'Mastered':
            final.append([row[0], str(val[4]), 1])
        else:
            final.append([row[0], str(val[4]), 0])

tlabels_df = pd.DataFrame(final, index=None, columns=['ConversationIDDataImpl', 'ConversationCorpus',
                                                      'Actively_listened_and_acknowledged_concerns'])


print('train label divide')
train_text = tlabels_df['ConversationCorpus'].tolist()
train_text = [' '.join(t.split()[0:200]) for t in train_text]
train_text = np.array(train_text, dtype=object)[:, np.newaxis]
train_label = tlabels_df['Actively_listened_and_acknowledged_concerns'].tolist()

print('model build')
input_text = layers.Input(shape=(1,), dtype="string")
embedding = ElmoEmbeddingLayer()(input_text)
dense = layers.Dense(256, activation='relu')(embedding)
pred = layers.Dense(1, activation='sigmoid')(dense)

model = Model(inputs=[input_text], outputs=pred)

# https://github.com/strongio/keras-elmo/blob/master/Elmo%20Keras.ipynb

def recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1(y_true, y_pred):
    prec = precision(y_true, y_pred)
    rec = recall(y_true, y_pred)
    return 2*((prec*rec)/(prec+rec+K.epsilon()))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', precision, recall, f1])
model.summary()

model.load_weights('ElmoModel_Version1.h5')

outs = model.predict(train_text[1:100])

i = 0
for row in train_text[1:100]:
    print(row, outs[i])
    i += 1
