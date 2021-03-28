from data_access import db

artistgenre_table = db.Table('ArtistsGenres',
                             db.Column('artist_id', db.Integer, db.ForeignKey('Artists.id'), primary_key=True),
                             db.Column('genre_id', db.Integer, db.ForeignKey('Genres.id'), primary_key=True)
                             )
