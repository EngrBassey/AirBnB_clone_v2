#!/usr/bin/python3
from flask import Flask
"""
Script that starts a Flask web application
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb", strict_slashes=False)
def second_route():
    return "<p>HBNB<p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
