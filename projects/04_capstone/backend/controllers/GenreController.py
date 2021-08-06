import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.GenreSchema import GenreSchema
from flask import request
from flask_restplus import Resource, Namespace, fields
from datetime import datetime

ns = Namespace("genres", description="Genres operations")

genre_fields = ns.model('Genre', {
    'id': fields.Integer,
    'name': fields.String
})

@ns.route("/<int:id>")
@ns.doc(params={'id': 'Genre id'})
class GenreController(Resource):
    @ns.response(200, 'Success', model = genre_fields)
    def get(self, id):
        genre = {"id": 1, "name": "Mystery"}
        return GenreSchema().dump(genre)

    @ns.expect(genre_fields)
    def patch(self, id):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data) # Add validation error
        print("genres/patch:")
        print(genre)
        pass

    def delete(self, id):
        pass
