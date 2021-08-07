from marshmallow import Schema, fields, validate, validates


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
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    birthday = fields.Date(required=True, format="%b %d %Y")
    sex = Sex(required=True)
    profile_url = fields.Str(required=False, data_key="profileUrl")
    photo_url = fields.Str(required=False, data_key="photoUrl")

    @validates("profile_url")
    def validate_profile_url(self, value):
        if value:
            validate.URL(error="Incorrect url").__call__(value)

    @validates("photo_url")
    def validate_photo_url(self, value):
        if value:
            validate.URL(error="Incorrect url").__call__(value)
