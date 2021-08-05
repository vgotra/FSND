from data_access import db
from data_access.entities import Genre, Language
from data_access.entities.MovieGenre import movie_genre_table
from data_access.entities.MovieLanguage import movie_language_table


class Movie(db.Model):
    __tablename__ = "Movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    release_date = db.Column(db.Date)
    release_country = db.Column(db.String(50))
    genres = db.relationship("Genre", secondary=movie_genre_table, back_populates="movies", lazy="joined")
    languages = db.relationship("Language", secondary=movie_language_table, back_populates="movies", lazy="joined")
