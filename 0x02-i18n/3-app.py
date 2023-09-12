#!/usr/bin/env python3
"""
this is where the app
is running
"""


from flask import Flask, request
from flask import render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    this is a config file
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


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
    home_title = gettext('Welcome to Holberton')
    home_header = gettext("Hello world!")
    result = {'home_title': home_title,
              'home_header': home_header
              }
    return render_template('3-index.html', result=result)


# if "__main__" == __name__:
#     app.run(debug=True)
