from data_access import db
from data_access.entities.ArtistGenre import artistgenre_table
from data_access.entities import City, Show, Genre


class Artist(db.Model, object):
    __tablename__ = 'Artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String(120))
    website_link = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=False)
    city = db.relationship('City', back_populates='artists', lazy='joined')
    shows = db.relationship('Show', back_populates='artist', lazy='joined')
    genres = db.relationship("Genre", secondary=artistgenre_table, back_populates="artists", lazy='joined')
