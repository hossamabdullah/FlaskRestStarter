import json
from app import app
from flask import request, jsonify
from werkzeug.datastructures import FileStorage
import os
from app.Sentiment import tweetSearch, tweetSentimentAnalysis

from flask_restplus import Api, Resource, fields, reqparse

api = Api(app, version='1.0', title='Sentiment API',
    description='API for performing sentiment analysis',
)

from app.Utils import Util

@api.route('/sentiment', endpoint = 'SentimentServiceAPI')
class SentimentServiceAPI(Resource):

    @api.doc(params={'keyword':'keyword to perform sentiment analysis on'})
    def post(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('keyword', required=True, help="keyword is required")
        args = self.parser.parse_args()
        tweetSearch(args["keyword"])
        sentiment = tweetSentimentAnalysis()
        return sentiment, 200



@api.route('/test', endpoint="test")
class ping(Resource):

    def get(self):
        return "hello", 200