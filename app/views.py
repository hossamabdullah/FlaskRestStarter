import json
from app import app
from flask import request, jsonify
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
import os


api = Api(app)

from models import Pet
from Utils import Util

class SentimentServiceAPI(Rsource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('keyword', location='json', required=True, help="keyword is required")

    def post(self):
        args = self.parser.parse_args()
        return args["keyword"], 200

api.add_resource(PetInsertionAPI, '/pet', endpoint = 'PetInsertionAPI')
