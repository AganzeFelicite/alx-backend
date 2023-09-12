#!/usr/bin/env python3
"""
this is where the app
is running
"""


from flask import Flask, request, g
from flask import render_template
from flask_babel import Babel

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
    locale = request.args.get('locale')
    if locale:
        return locale
    if g.user.get("locale") is not None:
        return g.user.get("locale")
    if request.headers.get("locale") is not None:
        return request.headers.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    this is a function that
    checks if the login is
    passed well
    """
    flag = request.args.get('login_as')
    try:
        return users.get(int(flag))
    except Exception:
        return None


@app.before_request
def before_request():
    """
    this is a function
    that runs before all
    the functioons
    """
    g.user = get_user()


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """
    simple hello world
    """
    return render_template('6-index.html')


# if "__main__" == __name__:
#     app.run(debug=True)
