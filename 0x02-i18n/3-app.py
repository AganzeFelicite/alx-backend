#!/usr/bin/env python3
"""
this is where the app
is running
"""


from flask import Flask, request
from flask import render_template
from flask_babel import Babel, gettext


app = Flask(__name__)



class Config:
    '''
    this is a config file
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determine the best match with our
    supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """
    simple hello world
    """
    return render_template('3-index.html')


# if "__main__" == __name__:
#     app.run(debug=True)
