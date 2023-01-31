#!/usr/bin/env python3
"""
starts a Flask web application
"""

from typing import Dict
from flask import Flask, g, request, render_template
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """
    Languages config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request() -> None:
    """
    Execute before the request
    """
    user = get_user()
    if user is not None:
        g.user = user


def get_user() -> Dict:
    """
    Get user data
    """
    try:
        u_id = request.args.get('login_as')
    except Exception:
        u_id = None
    if u_id is not None and u_id in users:
        return users[u_id]
    return None


@babel.localeselector
def get_locale():
    """
    Selecte best locale selector
    """
    try:
        lang = request.args.get('locale')
    except Exception:
        lang = None
    if lang is not None:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """returns template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
