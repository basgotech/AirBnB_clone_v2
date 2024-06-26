#!/usr/bin/python3
""" Starts a Flash Web App """
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello_hbnb():
    """ Prints a Message"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Fun """
    app.run(host='0.0.0.0', port=5000)
