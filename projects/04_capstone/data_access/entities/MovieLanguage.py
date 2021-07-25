from data_access import db

movie_language_table = db.Table('MoviesLanguages',
    db.Column('movie_id', db.Integer, db.ForeignKey('Movies.id'), primary_key=True),
    db.Column('language_id', db.Integer, db.ForeignKey('Languages.id'), primary_key=True)
)
