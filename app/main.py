#!/usr/bin/env python
from flask import (Flask, render_template, request, jsonify)
from peewee import IntegrityError
import bootstrap
from models.house import House
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)

bootstrap.initialize()


@app.route('/')
def index():
    avail_houses = House.select()
    return render_template('list_houses.html', houses=avail_houses)


@app.route('/houses/add', methods=['POST'])
def add_house():
    data = dict(request.form.items())
    try:
        House.create(
            plot_no=data.get('plot_no'),
            no_rooms=data.get('no_rooms'),
            rent=data.get('rent'),
            no_bathrooms=data.get('no_bathrooms'),
            location=data.get('location'),
            nearby_amenities=data.get('nearby_amenities'),
            rating=data.get('rating')
        )
        result = {'status': 'success'}
    except IntegrityError:
        result = {'status': 'failed', 'message': 'Plot number not unique'}
    finally:
        return jsonify(result)

if __name__ == '__main__':
    app.run(**app_start_config)
