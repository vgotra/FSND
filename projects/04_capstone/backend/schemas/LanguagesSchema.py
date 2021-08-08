from marshmallow import Schema, fields
from .LanguageSchema import LanguageSchema


class LanguagesSchema(Schema):
    items = fields.List(fields.Nested(LanguageSchema()), data_key="languages")
    page = fields.Int()
    pages = fields.Int()
    total = fields.Int()
