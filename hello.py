import os
from flask import Flask

app = Flask(__name__)
app._static_folder = 'static'

@app.route('/')
def hello():
    return 'Hello, World!'
