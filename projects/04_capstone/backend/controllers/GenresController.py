import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from schemas.GenreSchema import GenreSchema
from schemas.GenresSchema import GenresSchema
from flask import request
from flask_restx import Resource
from models.GenreModels import ns, genre_get, genre_put
from app import db
from data_access.repositories.GenresRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class GenresController(Resource):
    @ns.response(200, "Success", model=[genre_get])
    def get(self):
        genres = GenresRepository(db).get_all()
        #genres = [{"id": 1, "name": "Mystery"}, {"id": 2, "name": "Crime"}]
        return GenresSchema().dump(genres)

    @ns.expect(genre_put)
    @ns.response(200, "Success", model=genre_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data)  # Add validation error
        print("genres/put:")
        print(genre)
        return GenreSchema().dump(genre)
