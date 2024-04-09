#!/usr/bin/env python3
"""simple flask route"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
