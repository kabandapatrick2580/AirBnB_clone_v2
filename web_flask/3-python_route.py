#!/usr/bin/python3
"""script that starts web app"""
from flask import Flask
"""app instantiation"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displaying Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """displaying HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display C followed by a certain value of text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by value of text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
