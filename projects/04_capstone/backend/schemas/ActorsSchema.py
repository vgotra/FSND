from marshmallow import Schema, fields
from .ActorSchema import ActorSchema

class ActorsSchema(Schema):
    items = fields.List(fields.Nested(ActorSchema()), data_key="actors")
    page = fields.Int()
    pages = fields.Int()
    total = fields.Int()