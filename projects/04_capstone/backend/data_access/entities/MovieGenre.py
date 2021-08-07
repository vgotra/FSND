from data_access import db

movie_genre_table = db.Table("movies_genres", db.Column("movie_id", db.Integer, db.ForeignKey("movies.id"), primary_key=True), db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True))
