import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.MovieSchema import MovieSchema
from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime

ns = Namespace("movies", description="Movies operations")


@ns.route("/<int:id>")
@ns.doc(params={'id': 'Movie id'})
class MovieController(Resource):
    def get(self, id):
        movie = {"id": 1, "name": "The Usual Suspects"}
        return MovieSchema().dump(movie)

    def patch(self, id):
        json_data = request.get_json()
        movie = MovieSchema().load(json_data) # Add validation error
        print("movies/patch:")
        print(movie)
        pass

    def delete(self, id):
        pass
