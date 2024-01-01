#!/usr/bin/python3
"""script that starts web app and instrantiate an app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """the function displaying Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
