from flask import Flask, render_template, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    image = url_for('static', filename='drjohn.jpg')
    return render_template('index.html', imag=image)

def messageReceived(methods=['GET','POST']):
    print("Message was received")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):
    print("Received my event ", json)
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == "__main__":
    socketio.run(app, debug=True)