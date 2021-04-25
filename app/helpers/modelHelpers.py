import os
import json
from tensorflow import keras
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import pathlib


def loadModelAndTokenizer():
    # test 2
    document_path = os.getcwd() + "/app/models/"
    model = keras.models.load_model(document_path)
    with open(os.getcwd() + '/app/models/tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    return model, tokenizer
