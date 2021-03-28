from data_access import db

venuegenre_table = db.Table('VenuesGenres',
                            db.Column('venue_id', db.Integer, db.ForeignKey('Venues.id'), primary_key=True),
                            db.Column('genre_id', db.Integer, db.ForeignKey('Genres.id'), primary_key=True)
                            )
