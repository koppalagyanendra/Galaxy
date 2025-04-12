from application import db

class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    planets = db.relationship('Planet', backref='star', lazy='dynamic')

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)
    distance_from_star = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    color = db.Column(db.String(20), default='#4a90e2')  # Add default color
    star_id = db.Column(db.Integer, db.ForeignKey('star.id'), nullable=False)
