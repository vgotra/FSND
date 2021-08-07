import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.MovieSchema import MovieSchema
from flask import request
from flask_restplus import Resource
from models.MovieModels import ns, movie_get, movie_put


@ns.route("/")
@ns.response(401, "Authentication Error")
class MoviesController(Resource):
    @ns.response(200, "Success", model=[movie_get])
    def get(self):
        movies = [{"id": 1, "name": "The Usual Suspects"}, {"id": 2, "name": "The Matrix"}]
        return MovieSchema().dump(movies, many=True)

    @ns.expect(movie_put)
    @ns.response(200, "Success", model=movie_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data)  # Add validation error
        print("movies/put:")
        print(movie)
        pass
