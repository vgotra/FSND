import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.GenreSchema import GenreSchema
from schemas.GenresSchema import GenresSchema
from flask import request
from flask_restx import Resource
from models.GenreModels import ns, genre_get, genre_put, genres_get
from app import db
from data_access.repositories.GenresRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class GenresController(Resource):
    @ns.response(200, "Success", model=genres_get)
    def get(self):
        genres = GenresRepository(db).get_all()
        return GenresSchema().dump(genres)

    @requires_auth('put:genre')
    @ns.expect(genre_put)
    @ns.response(200, "Success", model=genre_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data)
        return GenreSchema().dump(genre)
