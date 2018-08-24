import json
from app import app
from flask import request, jsonify
from werkzeug.datastructures import FileStorage
import os
from app.Sentiment import Sentiment
from flask import jsonify
from flask_restplus import Api, Resource, fields, reqparse
from app.blockchain import Blockchain
api = Api(app, version='1.0', title='Sentiment API',
    description='API for performing sentiment analysis',
)

from app.Utils import Util

@api.route('/sentiment/online', endpoint = 'SentimentDetailsAPI')
class ValuesServicesAPI(Resource):

    @api.doc(params={'keyword':'keyword to perform sentiment analysis on'})
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('keyword', required=True, help="keyword is required")
        args = self.parser.parse_args()
        sentiment=Sentiment()

        sentiment.tweetSearch(args["keyword"])
        output = sentiment.tweetSentimentAnalysis()
        print("***************************")
        print(output['positive'],output['negative'] ,output['valuesSum'])
        print("***************************")        
        return output, 200

@api.route('/historyOfTopics', endpoint = 'SentimentApi')
class BlockChainTopic(Resource):

    @api.doc(params={'topic':'keyword to perform sentiment analysis on'})
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('topic', required=True, help="topic is required")
        args = self.parser.parse_args()
        blockchain=Blockchain()
        result=blockchain.return_topic(args["topic"])

        return result, 200

@api.route('/historyOfSentences', endpoint = 'historyOfSentences')
class BlockChainSentence(Resource):

    @api.doc(params={'topic':'topic to perform sentiment analysis on'})
    def get(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('topic', required=True, help="topic is required")
        args = self.parser.parse_args()
        blockchain=Blockchain()
        print(args["topic"])
        result=blockchain.return_sentence(args["topic"])

        return result, 200
