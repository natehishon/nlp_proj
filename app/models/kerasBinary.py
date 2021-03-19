import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import io
import json

# %matplotlib inline

df = pd.read_csv("../data/train-balanced-sarcasm.csv")

from sklearn.model_selection import train_test_split

df["comment"] = df["comment"].astype(str)

X = df['comment'].values

y = df['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

vocab_size = 10000
embedding_dim = 16
max_length = 32
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<oov>'
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(X_train)
word_index = tokenizer.word_index
training_sequences = tokenizer.texts_to_sequences(X_train)
training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
testing_sequences = tokenizer.texts_to_sequences(X_test)
testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# single_test = np.array(["Sounds like a really useful program."]) 76
# single_test = np.array(["oh you got me!"]) 38
# single_test = np.array(["I'm sorry, I totally should have done that!"]) 91
# single_test = np.array(["How did that get in there?"]) 30
# single_test = np.array(["that’ll be a stretch"]) 40
# single_test = np.array(["You are so smart."]) 61

# tokenizer.fit_on_texts(single_test)
# single_sequence = tokenizer.texts_to_sequences(single_test)
# single_padder = pad_sequences(single_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# print(single_padder.shape)
# print(model.predict(single_padder).shape)
# print(model.predict(single_padder))


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, Flatten

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
model.add(Flatten())
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(units=1, activation='sigmoid'))
opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
model.summary()

from tensorflow.keras.callbacks import EarlyStopping

model.fit(x=training_padded, y=y_train, batch_size=256, epochs=10, validation_data=(testing_padded, y_test), verbose=1,)

# save model and tokenizer

model.save('./')

tokenizer_json = tokenizer.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))

