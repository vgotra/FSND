from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('genres', description='Genres operations')

@ns.route('/<int:id>')
class Genre(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "Mystery"})

    def patch(self, id):
        pass

    def delete(self, id):
        pass