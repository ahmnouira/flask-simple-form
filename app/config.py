import os

# path of this file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    # sets MongoDB database
    MONGOALCHEMY_DATABASE = 'flask-simple-form'
    # send mail confi
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587 or 25  # 25 smtp port
    MAIL_USE_TLS =  True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ahmnouira@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') ## set it using export MAIL_PASSWORD=<your-email-password>
    
