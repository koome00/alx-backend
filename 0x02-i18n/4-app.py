#!/usr/bin/env python3
"""Babel configuration file"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    configuration class
    attributes:
        LANGUAGES: list
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object('1-app.Config')


@babel.localeselector
def get_locale():
    """
    get locale from request
    """
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    render index template
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
