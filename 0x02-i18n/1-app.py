#!/usr/bin/env python3

"""
This module sets up a basic Flask application with Babel for language localization.
"""

from flask import Flask, render_template
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

# Instantiate Babel
babel = Babel(app)

@app.route('/')
def index() -> str:
    """
    Render the main page of the app with a 'Hello world' message.
    
    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
