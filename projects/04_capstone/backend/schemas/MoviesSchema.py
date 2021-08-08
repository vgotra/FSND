from marshmallow import Schema, fields
from .MovieSchema import MovieSchema


class MoviesSchema(Schema):
    items = fields.List(fields.Nested(MovieSchema()), data_key="movies")
    page = fields.Int()
    pages = fields.Int()
    total = fields.Int()
