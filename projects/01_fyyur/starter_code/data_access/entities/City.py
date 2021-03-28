from data_access import db
from data_access.entities import Artist, Venue


class City(db.Model):
    __tablename__ = 'Cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    state = db.Column(db.String(2))
    artists = db.relationship('Artist', back_populates='city', lazy=True)
    venues = db.relationship('Venue', back_populates='city', lazy=True)
