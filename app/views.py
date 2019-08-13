from flask import render_template, redirect, url_for
from app import app
from app.forms import UserForm
from app.models import Users as User
from app.mail import send_mail
from app.time_socket import *

@app.route("/", methods=['GET', 'POST'])
def index():

    form = UserForm()

    time_dict()

    if form.validate_on_submit():
        company = "" if form.company.data is None else form.company.data
        city = "" if form.city.data is None else form.city.data
        state = "" if form.state.data is None else form.state.data
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    password=form.password.data, company=company, city=city, state=state)
        user.set_password(form.password.data)
        print("USER-->", user)
        user.save()
        send_to_user = User.query.filter(User.email == user.email).first()
        if send_to_user:
            send_mail(user)
            print ('SEND_TO-->', send_to_user.first_name + " " + send_to_user.last_name)
        return redirect(url_for('registered'))
    return render_template('index.html', form=form, time=time)


@app.route("/registered/", methods=['GET', 'POST'])
def registered():
    time_dict()

    return render_template('registered.html', time=time)
