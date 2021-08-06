import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.GenreSchema import GenreSchema
from flask import request
from flask_restplus import Resource
from models.GenreModels import ns, genre_fields

@ns.route("/")
class GenresController(Resource):
    @ns.response(200, 'Success', model = [genre_fields])
    def get(self):
        genres = [{"id": 1, "name": "Mystery"}, {"id": 2, "name": "Crime"}]
        return GenreSchema().dump(genres, many=True)

    @ns.expect(genre_fields)
    @ns.response(200, 'Success')
    @ns.response(400, 'Validation Error')
    def put(self):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data) # Add validation error
        print("genres/put:")
        print(genre)
        pass
