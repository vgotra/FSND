from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    description = fields.Str(required=False, dump_default=None, load_default=None)
    release_date = fields.Date(required=False, dump_default=None, load_default=None, data_key="releaseDate")
    release_country = fields.Str(required=False, dump_default=None, load_default=None, data_key="releaseCountry")
