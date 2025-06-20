# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello from Python Microservice 2! Env: {os.getenv('APP_ENV')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
