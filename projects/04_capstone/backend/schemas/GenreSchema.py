from marshmallow import Schema, fields


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    # movies = db.relationship("Movie", secondary=movie_genre_table, back_populates="genres")
