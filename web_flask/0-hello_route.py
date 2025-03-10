#!/usr/bin/python3
"""Starts Flask web app,
   listening on 0.0.0.0:5000, 
   route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    