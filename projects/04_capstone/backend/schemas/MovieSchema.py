from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str()
    release_date = fields.Date()
    release_country = fields.Str()
    # genres = db.relationship("Genre", secondary=movie_genre_table, back_populates="movies", lazy="joined")
    # languages = db.relationship("Language", secondary=movie_language_table, back_populates="movies", lazy="joined")
