#!/usr/bin/python3
# simple flask app
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text=None):
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_template(n):
    return render_template('6-number_odd_or_even.html',
                           number=n,
                           is_odd="odd" if n % 2 == 1 else "even"
                           )


app.run(debug=True)
