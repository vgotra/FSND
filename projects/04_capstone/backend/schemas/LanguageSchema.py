from marshmallow import Schema, fields


class LanguageSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    #movies = db.relationship("Movie", secondary=movie_language_table, back_populates="languages")