import os
from flask import Flask, jsonify

PORT = int(os.environ.get('APP_PORT', 5000))
PONG_MESSAGE = os.environ.get('PONG_MESSAGE', 'pong')

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({
        'message': 'Привет! Используй /ping для проверки',
        'endpoints': {
            '/ping': 'возвращает PONG_MESSAGE',
            '/health': 'проверка здоровья'
        }
    })

@app.route('/ping')
def ping():
    return jsonify({
        'status': 'ok',
        'response': PONG_MESSAGE,
        'port': PORT
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'port': PORT})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)

