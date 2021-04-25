"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource

from .security import require_auth
from . import api_rest

# todo move me to a better place
from app.helpers import modelHelpers
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()

        model, tokenizer = modelHelpers.loadModelAndTokenizer()

        test_sentence = np.array(["I'm sorry, I totally should have done that!"])

        max_length = 32
        trunc_type = 'post'
        padding_type = 'post'

        tokenizer.fit_on_texts(test_sentence)
        single_sequence = tokenizer.texts_to_sequences(test_sentence)
        single_padder = pad_sequences(single_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

        prediction = print(model.predict(single_padder))

        return prediction

    def post(self, resource_id):
        json_payload = request.json

        # get input sentence

        # access saved model

        # run sentence through model

        # return output

        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}
