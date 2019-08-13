from flask import Flask
from app.config import Config
from flask_mongoalchemy import MongoAlchemy
from flask_socketio import SocketIO
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = MongoAlchemy(app)
socketio = SocketIO(app)
mail = Mail(app)

from app import models, views
