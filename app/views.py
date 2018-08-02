import json
from app import app
from flask import request, jsonify
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
import os
from app.Sentiment import tweetSearch, tweetSentimentAnalysis

api = Api(app)

from app.Utils import Util

class SentimentServiceAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('keyword', required=True, help="keyword is required")

    def post(self):
        args = self.parser.parse_args()
        tweetSearch(args["keyword"])
        sentiment = tweetSentimentAnalysis()
        return sentiment, 200

api.add_resource(SentimentServiceAPI, '/sentiment', endpoint = 'SentimentServiceAPI')
