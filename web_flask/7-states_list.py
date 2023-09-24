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
    unsorted_states = storage.all(State)
    sorted_states = []
    for state in unsorted_states.items():
        sorted_states.append({
            'id': state[1].id,
            'name': state[1].name
        })
        state[1].name
    print(sorted_states)
    return render_template('7-states_list.html',
                           states=sorted_states
                           )


app.run(debug=True)
