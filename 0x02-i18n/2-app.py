#!/usr/bin/env python3
"""Babel configuration file"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    configuration class
    attributes:
        LANGUAGES: list
    """
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """
    get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    render index template
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
