import os
import sys

from flask.json import jsonify

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.GenreSchema import GenreSchema
from flask import request
from flask_restx import Resource
from models.GenreModels import ns, genre_get, genre_patch
from app import db
from data_access.repositories.GenresRepository import *
from common.exceptions.ApiError import ApiError


@ns.route("/<int:id>")
@ns.doc(params={"id": "Genre id"})
@ns.response(401, "Authentication Error")
@ns.response(404, "Not Found")
class GenreController(Resource):
    @requires_auth("get:genre-details")
    @ns.response(200, "Success", model=genre_get)
    def get(self, id):
        genre = GenresRepository(db).get(id)
        if not genre:
            raise ApiError("Genre is not found", 404)
        return GenreSchema().dump(genre)

    @requires_auth("put:genre")
    @ns.expect(genre_patch)
    @ns.response(200, "Success", model=genre_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        genre = GenreSchema().load(json_data)
        try:
            genre_db = GenresRepository(db).update(id, genre)
            return GenreSchema().dump(genre_db)
        except NotFound:
            raise ApiError("Genre is not found", 404)

    @requires_auth("delete:genre")
    def delete(self, id):
        try:
            deleted_id = GenresRepository(db).delete(id)
            return jsonify({"id": deleted_id})
        except NotFound:
            raise ApiError("Genre is not found", 404)
