from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace("movies", description="Movies operations")


@ns.route("/<int:id>")
class MovieController(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "The Usual Suspects"})

    def patch(self, id):
        pass

    def delete(self, id):
        pass
