#! /bin/sh
export FLASK_APP=app.py
export MAIL_PASSWORD=<your-email-password>
gunicorn -b 0.0.0.0:5000  --worker-class eventlet -w 1 --access-logfile - --error-logfile - app:app
