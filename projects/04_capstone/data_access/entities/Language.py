from data_access import db
from data_access.entities.MovieLanguage import movie_language_table

class Language(db.Model):
    __tablename__ = 'Languages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    movies = db.relationship("Movie", secondary=movie_language_table, back_populates="languages")
