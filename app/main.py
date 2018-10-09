#!/usr/bin/env python
from flask import (Flask, render_template, request, jsonify)
import bootstrap
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)

bootstrap.initialize()
@app.route('/')
def index():
    return render_template('list_houses.html')


if __name__ == '__main__':
    app.run(**app_start_config)
