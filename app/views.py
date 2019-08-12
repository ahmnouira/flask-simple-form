
from flask import render_template, redirect, url_for
from app.forms import UserForm
from app.models import Users as User
from datetime import datetime as dt
from flask_socketio import SocketIO, emit
from app import app
socketio = SocketIO(app)
thread = None
time = {}


def time_dict():
    global time
    time = {
        'day_name': str(dt.strftime(dt.now(), '%A')),
        'month': str(dt.strftime(dt.now(), '%B')),
        'day': str(dt.now().day),
        'year': str(dt.now().year),
        'hour': str(dt.now().hour),
        'minute': str(dt.strftime(dt.now(), '%M')),
        'second': str(dt.strftime(dt.now(), '%S')),
        'pm_am': str(dt.strftime(dt.now(), '%P'))
    }


def background_thread():
    while True:

        socketio.sleep(1)

        time_dict()

        """
            On every seconds, the server send message to the client with updated time.
            First parameter of emit function tells which function to call on client side.
          
        """
        socketio.emit('my_response',
                      {'data': 'Message from server', 'time': time},
                      namespace='/test')


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
        return redirect(url_for('registered'))
    return render_template('index.html', form=form, time=time)


@app.route("/registered/", methods=['GET', 'POST'])
def registered():
    time_dict()

    return render_template('registered.html', time=time)


@socketio.on('connect', namespace='/test')
def test_connect():
    time_dict()
    global thread
    if thread is None:
        # Once any client is connected, the background_thread function starts in loop
        thread = socketio.start_background_task(target=background_thread)

    socketio.emit('my_response',
                  {'data': 'Message from server', 'time': time},
                  namespace='/test')
