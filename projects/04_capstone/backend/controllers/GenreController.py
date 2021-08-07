import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.GenreSchema import GenreSchema
from flask import request
from flask_restx import Resource
from models.GenreModels import ns, genre_get, genre_patch


@ns.route("/<int:id>")
@ns.doc(params={"id": "Genre id"})
@ns.response(401, "Authentication Error")
class GenreController(Resource):
    @ns.response(200, "Success", model=genre_get)
    def get(self, id):
        genre = {"id": 1, "name": "Mystery"}
        return GenreSchema().dump(genre)

    @ns.expect(genre_patch)
    @ns.response(200, "Success", model=genre_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data)  # Add validation error
        print("genres/patch:")
        print(genre)

    def delete(self, id):
        pass
