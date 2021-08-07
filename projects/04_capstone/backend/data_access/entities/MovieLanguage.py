from data_access import db

movie_language_table = db.Table("movies_languages", db.Column("movie_id", db.Integer, db.ForeignKey("movies.id"), primary_key=True), db.Column("language_id", db.Integer, db.ForeignKey("languages.id"), primary_key=True))
