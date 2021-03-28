from data_access import db
from data_access.entities.ArtistGenre import artistgenre_table
from data_access.entities.VenueGenre import venuegenre_table


class Genre(db.Model):
    __tablename__ = 'Genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    venues = db.relationship("Venue", secondary=venuegenre_table, back_populates="genres")
    artists = db.relationship("Artist", secondary=artistgenre_table, back_populates="genres")
