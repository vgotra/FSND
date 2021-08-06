from flask_restplus import Resource, Namespace, fields

ns = Namespace("genres", description="Genres operations")

genre_fields = ns.model('Genre', {
    'id': fields.Integer,
    'name': fields.String
})
