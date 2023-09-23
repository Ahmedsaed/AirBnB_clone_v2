#!/usr/bin/python3
# simple flask app
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


app.run(debug=True)
