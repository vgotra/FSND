import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.MovieSchema import MovieSchema
from flask import request
from flask_restplus import Resource
from models.MovieModels import ns, movie_get, movie_patch


@ns.route("/<int:id>")
@ns.doc(params={"id": "Movie id"})
@ns.response(401, "Authentication Error")
class MovieController(Resource):
    @ns.response(200, "Success", model=movie_get)
    def get(self, id):
        movie = {"id": 1, "name": "The Usual Suspects"}
        return MovieSchema().dump(movie)

    @ns.expect(movie_patch)
    @ns.response(200, "Success", model=movie_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data)  # Add validation error
        print("movies/patch:")
        print(movie)
        pass

    def delete(self, id):
        pass
