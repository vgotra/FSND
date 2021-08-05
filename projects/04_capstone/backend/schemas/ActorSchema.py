from marshmallow import Schema, fields, validate


class Sex(fields.Field):
    """Sex field that deserializes to a Sex object."""

    def _deserialize(self, value, *args, **kwargs):
        if value == "Male":
            return True
        else:
            return False

    def _serialize(self, value, *args, **kwargs):
        if value:
            return "Male"
        return "Female"


class ActorSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    birthday = fields.Date(required=True)
    sex = Sex(required=True)
    profile_url = fields.Str(data_key="profileUrl", validate=validate.URL(error="Incorrect url"))
    photo_url = fields.Str(data_key="photoUrl", validate=validate.URL(error="Incorrect url"))
