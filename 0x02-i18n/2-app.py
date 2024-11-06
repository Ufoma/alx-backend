#!/usr/bin/env python3

"""
This module sets up a Flask application with Babel for language localization.
It includes a locale selection feature based on user request headers.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List

class Config:
    """
    Configuration class for language and timezone settings.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the user's request.

    Returns:
        str: Best-matched language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render the main page of the app with a 'Hello world' message.
    
    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)
