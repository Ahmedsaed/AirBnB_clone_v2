#!/usr/bin/python3
""" simple flask app """
from flask import Flask, request
from models import storage
from models import *
from flask import render_template
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template("9-states.html", states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
