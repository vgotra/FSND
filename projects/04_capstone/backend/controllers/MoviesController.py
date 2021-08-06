import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.MovieSchema import MovieSchema
from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime


ns = Namespace("movies", description="Movies operations")


@ns.route("/")
class MoviesController(Resource):
    @ns.doc("List all movies")
    def get(self):
        movies = [{"id": 1, "name": "The Usual Suspects"}, {"id": 2, "name": "The Matrix"}]
        return MovieSchema().dump(movies, many=True)

    def put(self):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data) # Add validation error
        print("movies/put:")
        print(movie)
        pass
