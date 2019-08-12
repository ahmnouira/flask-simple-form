from app import app
from app.views import socketio


if __name__ == '__main__':
    socketio.run(app)
