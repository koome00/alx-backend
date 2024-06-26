#!/usr/bin/env python3
"""Babel configuration file"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    render index template
    """
    return render_template("8-index.html")


def get_user():
    """
    returns a user dictionary or None if the
    ID cannot be found or if login_as was not passed
    """
    user_id = request.args.get('login_as', None)
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    force get_use to execute first
    """
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone():
    """
    handle correct timezone
    """
    t_zone = request.args.get('timezone', None)
    if t_zone:
        try:
            return timezone(t_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    if g.user:
        try:
            t_zone = g.user.get('timezone')
            return timezone(t_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    return request.accept_languages.best_match(app.config[
        'BABEL_DEFAULT_TIMEZONE'])


if __name__ == "__main__":
    app.run()
