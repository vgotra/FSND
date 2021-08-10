from marshmallow import Schema, fields


class LanguageSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
