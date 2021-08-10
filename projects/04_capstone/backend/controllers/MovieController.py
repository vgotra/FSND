import os
import sys

from flask.json import jsonify

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.MovieSchema import MovieSchema
from flask import request
from flask_restx import Resource
from models.MovieModels import ns, movie_get, movie_patch
from app import db
from data_access.repositories.MoviesRepository import *
from common.exceptions.ApiError import ApiError
from data_access.exceptions.NotFound import NotFound


@ns.route("/<int:id>")
@ns.doc(params={"id": "Movie id"})
@ns.response(401, "Authentication Error")
@ns.response(404, "Not Found")
class MovieController(Resource):
    @requires_auth("get:movie-details")
    @ns.response(200, "Success", model=movie_get)
    def get(self, id):
        movie = MoviesRepository(db).get(id)
        if not movie:
            raise ApiError("Movie is not found", 404)
        return MovieSchema().dump(movie)

    @requires_auth("patch:movie")
    @ns.expect(movie_patch)
    @ns.response(200, "Success", model=movie_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data)
        try:
            movie_db = MoviesRepository(db).update(id, movie)
            return MovieSchema().dump(movie_db)
        except NotFound:
            raise ApiError("Movie is not found", 404)

    @requires_auth("delete:movie")
    def delete(self, id):
        try:
            deleted_id = MoviesRepository(db).delete(id)
            return jsonify({"id": deleted_id})
        except NotFound:
            raise ApiError("Movie is not found", 404)
