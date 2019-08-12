from flask import Flask
from app.config import Config
from flask_mongoalchemy import MongoAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = MongoAlchemy(app)


from app import models, views
