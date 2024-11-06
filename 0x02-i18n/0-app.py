#!/usr/bin/env python3

"""
This module sets up a basic Flask web application with a single route.
It displays a simple "Hello world" message on the main page.
"""

from flask import Flask, render_template
from typing import Any

app = Flask(__name__)

@app.route('/')
def index() -> Any:
    """
    Render the main page of the app with a 'Hello world' message.
    
    Returns:
        Any: Rendered HTML template for the main page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
