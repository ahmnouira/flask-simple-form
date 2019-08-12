#! /bin/sh

gunicorn -b 0.0.0.0:5000  --worker-class eventlet -w 1 --access-logfile - --error-logfile - app:app
