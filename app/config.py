import os

# path of this file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    # sets MongoDB database
    MONGOALCHEMY_DATABASE = 'flask-simple-form'
