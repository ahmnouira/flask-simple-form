# Flask Simple From 
This is a simple flask register-form application designed to run in multiple ways: 

# Overview
![index](/img/index.png)

# Running this app

This app is designed to run in different ways:
1. As a standalone app running on your machine

## 1. As a standalone app

1. install [python](https://www.python.org/) 
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements/dev.txt` to install the app libaries and it dependencies

### running the app

* After installing, you need to set your application _environment variable_ by running `export FLASK_APP=app.py`
* run the server using `flask run --reload --debugger`
* Access the running app in a browser at the URL written to the console (most likely http://localhost:5000)
 
