#!/usr/bin/env python3
"""Babel configuration file"""
from flask import Flask, render_template
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


@app.route("/")
def index():
    """
    render index template
    """
    return render_template("0-index.html")
