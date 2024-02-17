#!/usr/bin/python3
"""start flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display C"""
    return "C {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
