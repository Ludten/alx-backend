#!/usr/bin/env python3
"""
starts a Flask web application
"""

from flask import Flask, request, render_template
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Selecte best locale selector
    """
    lang = request.args.get('locale')
    if lang is None:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return request.accept_languages.best_match(lang)


@app.route('/', strict_slashes=False)
def index():
    """returns template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
