import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(hello="world")

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}