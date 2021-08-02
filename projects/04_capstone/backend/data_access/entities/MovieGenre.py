from data_access import db

movie_genre_table = db.Table("MoviesGenres", db.Column("movie_id", db.Integer, db.ForeignKey("Movies.id"), primary_key=True), db.Column("genre_id", db.Integer, db.ForeignKey("Genres.id"), primary_key=True))
