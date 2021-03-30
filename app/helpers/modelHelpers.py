import os
import json
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import tokenizer_from_json
import pathlib


def loadModelAndTokenizer():

    cwd = pathlib.Path().parent.absolute()
    model_location = os.path.abspath(os.path.join(os.path.dirname(cwd), "models"))
    print(f"cwd is {cwd} model location is {model_location}")

    """    
model = keras.models.load_model('/Users/michael/nlpFinal/nlp_proj/app/models')
    # /Users/nathanhishon/Development/NLP_py/project2/flask-vuejs-template/app/models/
    # /Users/nathanhishon/Development/NLP_py/project2/flask-vuejs-template/app/models/tokenizer.json
    # /Users/michael/nlpFinal/nlp_proj/app/models/tokenizer.json
    with open('/Users/michael/nlpFinal/nlp_proj/app/models/tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    """
    model, tokenizer = "model", "tokenizer"
    return model, tokenizer
