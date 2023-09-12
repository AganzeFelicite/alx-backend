#!/usr/bin/env python3
"""
this is where the app
is running
"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """
    simple hello world
    """
    return render_template('0-index.html')
