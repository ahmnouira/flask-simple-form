from app import socketio
from flask_socketio import emit
from datetime import datetime as dt


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
