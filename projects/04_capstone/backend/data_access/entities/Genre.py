from data_access import db
from data_access.entities.MovieGenre import movie_genre_table


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movies = db.relationship("Movie", secondary=movie_genre_table, back_populates="genres")
