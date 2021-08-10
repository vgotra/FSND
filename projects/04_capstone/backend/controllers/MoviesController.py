import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.MovieSchema import MovieSchema
from schemas.MoviesSchema import MoviesSchema
from flask import request
from flask_restx import Resource
from models.MovieModels import ns, movie_get, movie_put, movies_get
from app import db
from data_access.repositories.MoviesRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class MoviesController(Resource):
    @ns.response(200, "Success", model=movies_get)
    def get(self):
        movies = MoviesRepository(db).get_all()
        return MoviesSchema().dump(movies)

    @requires_auth("put:movie")
    @ns.expect(movie_put)
    @ns.response(200, "Success", model=movie_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data)
        movie_db = MoviesRepository(db).create(movie)
        return MovieSchema().dump(movie_db)
