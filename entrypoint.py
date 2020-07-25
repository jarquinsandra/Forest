"""

AUTOR: jarquinsandra


"""
import os
from app import create_app
from flask import render_template




settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')