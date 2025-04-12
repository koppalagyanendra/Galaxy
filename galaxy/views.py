from flask import render_template, request, redirect, url_for, jsonify, Blueprint
from galaxy.models import db, Star, Planet

galaxy_app = Blueprint('galaxy_app', __name__)

import random

# Predefined list of planet colors
PLANET_COLORS = [
    "#bdbdbd",  # Mercury - gray
    "#ffcc00",  # Venus - yellow
    "#4caf50",  # Earth - green
    "#e53935",  # Mars - red
    "#ff9800",  # Jupiter - orange
    "#ffeb3b",  # Saturn - pale yellow
    "#00bcd4",  # Uranus - cyan
    "#0000ff",  # Neptune - blue
    "#9c27b0",  # Bonus - purple
    "#795548",  # Bonus - brown
]


# Route to display galaxy (all stars and planets)
@galaxy_app.route('/')
def galaxy():
    stars = Star.query.all()
    planets = Planet.query.all()
    return render_template('galaxy.html', stars=stars, planets=planets)

# Route to view details of a star or planet (click for details)
@galaxy_app.route('/details/<type>/<int:id>')
def details(type, id):
    if type == 'star':
        obj = Star.query.get_or_404(id)
    elif type == 'planet':
        obj = Planet.query.get_or_404(id)
    return jsonify({
        'name': obj.name,
        'size': obj.size,
        'distance': obj.distance if type == 'star' else obj.distance_from_star,
        'description': obj.description
    })

# Route to add a new star
@galaxy_app.route('/add/star', methods=['GET', 'POST'])
def add_star():
    if request.method == 'POST':
        star = Star(
            name=request.form['name'],
            size=float(request.form['size']),
            distance=float(request.form['distance']),
            description=request.form['description']
        )
        db.session.add(star)
        db.session.commit()
        return redirect(url_for('galaxy_app.galaxy'))  # Use correct blueprint reference
    return render_template('add_star.html')


@galaxy_app.route('/add/planet', methods=['GET', 'POST'])
def add_planet():
    if request.method == 'POST':
        random_color = random.choice(PLANET_COLORS)
        planet = Planet(
            name=request.form['name'],
            size=float(request.form['size']),
            distance_from_star=float(request.form['distance']),
            description=request.form['description'],
            star_id=int(request.form['star_id']),
            color=random_color  # Auto-assigned random color
        )
        db.session.add(planet)
        db.session.commit()
        return redirect(url_for('galaxy_app.galaxy'))

    stars = Star.query.all()
    return render_template('add_planet.html', stars=stars)
