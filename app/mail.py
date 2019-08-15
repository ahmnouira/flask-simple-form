from app import app, mail
from flask_mail import Message
from flask import render_template
from threading import Thread

def send_email_helper(subject , sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_sync_email, args=(app, msg)).start()


def send_sync_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(user):
    send_email_helper(' [flask-simple-form] ', sender=app.config['MAIL_USERNAME'], \
    recipients=[user.email], text_body = render_template('email/register_notification.txt', user=user),
    html_body = render_template('email/register_notification.html', user=user))
