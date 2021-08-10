from marshmallow import Schema, fields


class GenreSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
