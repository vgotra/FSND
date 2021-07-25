from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('genres', description='Genres operations')

@ns.route('/<int:id>')
class Genre(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "Mystery"})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass