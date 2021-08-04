from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace("movies", description="Movies operations")


@ns.route("/")
class MoviesController(Resource):
    @ns.doc("List all movies")
    def get(self):
        return jsonify([{"id": 1, "name": "The Usual Suspects"}, {"id": 2, "name": "The Matrix"}])

    def put(self):
        pass
