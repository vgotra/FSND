from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    release_date = fields.Date(required=False, data_key="releaseDate")
    release_country = fields.Str(required=False, data_key="releaseCountry")
    # genres = db.relationship("Genre", secondary=movie_genre_table, back_populates="movies", lazy="joined")
    # languages = db.relationship("Language", secondary=movie_language_table, back_populates="movies", lazy="joined")
