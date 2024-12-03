from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)

CONFIG_FILE = 'config.json'

@app.route('/')
def index():
    return render_template('index.html')

def update_config(data):
    """Функция для обновления конфигурации на клиентах."""
    socketio.emit('update', data)  # Отправка обновленных данных всем клиентам

if __name__ == "__main__":
    socketio.run(app, debug=True)
    print("Запущено!")