#!/usr/bin/env python3
"""
this is where the app
is running
"""


from flask import Flask
from flask import render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class config:
    '''
    this is a config file
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(config)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """
    simple hello world
    """
    return render_template('1-index.html')

# if "__main__" == __name__:
#     app.run(debug=True)
