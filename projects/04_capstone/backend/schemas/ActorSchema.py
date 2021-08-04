from marshmallow import Schema, fields


class Sex(fields.Field):
    """Sex field that deserializes to a Sex object."""
    def _deserialize(self, value, *args, **kwargs):
        if value == "Female":
            return False
        else:
            return True
    def _serialize(self, value, *args, **kwargs):
        if not value:
            return "Female"
        return "Male"


class ActorSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    birthday = fields.Date(required=True)
    sex = Sex(required=True)
    profile_url = fields.Url()
    photo_url = fields.Url()