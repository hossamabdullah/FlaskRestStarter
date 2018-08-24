from flask import Flask
from mongoengine import connect
from flask_cors import CORS

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.config.from_object('config')
connect(host=app.config["DATABASE_URI"])

from app import views
