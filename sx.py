from flask import Flask, render_template
from threading import Lock
from flask_socketio import SocketIO, emit

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

@app.route("/")
def main():
    return render_template('index.html')

@socketio.on('my_broadcast_event')
def test_connect(message):
    #print("Welcome, aaa received")
    print(message['data'])
    emit('sent', {'data': 'Server'})

if __name__ == '__main__':
    socketio.run(app, port=8000)
    #app.run(port = 8000)