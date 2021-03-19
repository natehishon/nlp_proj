import os
import json
from tensorflow import keras
from tensorflow.keras.preprocessing.text import tokenizer_from_json


def loadModelAndTokenizer():

    model = keras.models.load_model('/Users/nathanhishon/Development/NLP_py/project2/flask-vuejs-template/app/models/')

    with open('/Users/nathanhishon/Development/NLP_py/project2/flask-vuejs-template/app/models/tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    return model, tokenizer
