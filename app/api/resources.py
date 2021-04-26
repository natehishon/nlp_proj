"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restx import Resource
from flask import jsonify
import json
import os


from .security import require_auth
from . import api_rest

# todo move me to a better place
from app.helpers import modelHelpers
from app.helpers import textHelper
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import pipeline



class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):

        model, tokenizer = modelHelpers.loadModelAndTokenizer()
        input = "Sounds like a really useful program"

        test_sentence = np.array([input])

        max_length = 32
        trunc_type = 'post'
        padding_type = 'post'

        tokenizer.fit_on_texts(test_sentence)
        single_sequence = tokenizer.texts_to_sequences(test_sentence)
        single_padder = pad_sequences(single_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

        prediction = model.predict(single_padder)

        sentiment_analysis = pipeline("sentiment-analysis")
        sentiment = sentiment_analysis(input)[0]


        response = dict()

        sentiment['score'] = str("{:.2%}".format(sentiment['score']))

        response['predict'] = str("{:.2%}".format(prediction[0][0]))
        response['sentiment'] = sentiment
        response['sentence'] = textHelper.getTextOutput(input)

        return jsonify(response)

    def post(self, resource_id):

        model, tokenizer = modelHelpers.loadModelAndTokenizer()
        input = request.json['sentence']

        print(input)
        test_sentence = np.array([input])

        max_length = 32
        trunc_type = 'post'
        padding_type = 'post'

        tokenizer.fit_on_texts(test_sentence)
        single_sequence = tokenizer.texts_to_sequences(test_sentence)
        single_padder = pad_sequences(single_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

        prediction = model.predict(single_padder)

        sentiment_analysis = pipeline("sentiment-analysis")
        sentiment = sentiment_analysis(input)[0]

        response = dict()

        sentiment['score'] = str("{:.2%}".format(sentiment['score']))

        response['predict'] = str("{:.2%}".format(prediction[0][0]))
        response['sentiment'] = sentiment
        response['sentence'] = textHelper.getTextOutput(input)

        return jsonify(response)


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}
