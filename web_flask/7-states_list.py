#!/usr/bin/python3
"""
Display a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def ream_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects."""
    states = storage.all("State").values()
    arr_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=arr_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
