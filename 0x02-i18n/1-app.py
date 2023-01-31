#!/usr/bin/env python3
"""
starts a Flask web application
"""

from typing import Union
from flask import Flask, request, render_template
from flask_babel import Babel


class Config():
    """
    Languages config class
    """
    LANGUAGES = ["en", "fr"]
    TIMEZONE = 'UTC'


def get_locale() -> Union[str, None]:
    """
    set locale selector
    """
    return request.accept_languages.best_match(Config.LANGUAGES[0])


def get_timezone() -> str:
    """
    Return timezone
    """
    return Config.TIMEZONE


app = Flask(__name__)
babel = Babel(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone
)


@app.route('/', strict_slashes=False)
def index():
    """returns template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
