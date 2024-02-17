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
    return "C {}".format(escape(text.replace("_", " ")))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display python"""
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """display number"""
    if (isinstance(escape(n.replace("_", " ")), int)):
        return "{} is a number".format(escape(n.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
