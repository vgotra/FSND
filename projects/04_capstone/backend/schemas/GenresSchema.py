from marshmallow import Schema, fields
from .GenreSchema import GenreSchema


class GenresSchema(Schema):
    items = fields.List(fields.Nested(GenreSchema()), data_key="genres")
    page = fields.Int()
    pages = fields.Int()
    total = fields.Int()
