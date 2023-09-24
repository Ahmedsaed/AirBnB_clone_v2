#!/usr/bin/python3
# simple flask app
from flask import Flask, request
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


app.run(debug=True)
