from data_access import db
from data_access.entities.VenueGenre import venuegenre_table
from data_access.entities import City, Show, Genre

class Venue(db.Model):
    __tablename__ = 'Venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String(120))
    address = db.Column(db.String(120))
    website_link = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=False)
    city = db.relationship('City', back_populates='venues', lazy='joined')
    shows = db.relationship('Show', back_populates='venue', lazy='joined')
    genres = db.relationship("Genre", secondary=venuegenre_table, back_populates="venues", lazy='joined')
