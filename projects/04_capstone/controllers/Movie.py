from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('movies', description='Movies operations')

@ns.route('/<int:id>')
class Movie(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "The Usual Suspects"})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass