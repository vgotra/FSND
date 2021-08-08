import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from schemas.MovieSchema import MovieSchema
from flask import request
from flask_restx import Resource
from models.MovieModels import ns, movie_get, movie_patch
from app import db
from data_access.repositories.MoviesRepository import *


@ns.route("/<int:id>")
@ns.doc(params={"id": "Movie id"})
@ns.response(401, "Authentication Error")
class MovieController(Resource):
    @ns.response(200, "Success", model=movie_get)
    def get(self, id):
        movie = MoviesRepository(db).get(id)
        return MovieSchema().dump(movie)

    @ns.expect(movie_patch)
    @ns.response(200, "Success", model=movie_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data)
        return MovieSchema().dump(movie)

    def delete(self, id):
        pass
