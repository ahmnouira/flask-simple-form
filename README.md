# flask-simple-form
This is a simple flask register-form application designed to run in multiple ways

# Notes
* This app use _[MongoDB](https://www.mongodb.com/)_ as database supported by _[Flask-MongoAlchemy](https://pythonhosted.org/Flask-MongoAlchemy/)_ extension
=> So you have to install **MongoDB** database to run this locally 
 
* uses _[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)_ along with _[Ajax](https://en.wikipedia.org/wiki/Ajax_(programming))_ for real time update

* you will get an email if you have registered 

# Overview
![index](/img/index.png)
![registered](/img/registered.png)
![email](/img/email.png)

# Running this app


This app is designed to run in different ways:
1. As a standalone app running on your machine

## 1. As a standalone app

1. install [python](https://www.python.org/) 
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements/prod_local.txt` to install the app libaries and it dependencies
6. install MongoDB database `sudo apt-get install mongodb`
7. check your database is installed and print its version using `mongo --version`

### running the app

* After installing, you need to set your application _environment variable_ by running `export FLASK_APP=app.py`
* run `export MAIL_PASSWORD=<your-email-password>` to set your email password _environment variable_ 
* run the server using the script file `run.sh` by typing `./run`
* Access the running app in a browser at the URL written to the console (most likely http://0.0.0.0:5000)
 
