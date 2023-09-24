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


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
