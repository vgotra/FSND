from flask import jsonify
from flask_restplus import Resource, Namespace, fields

ns = Namespace('genres', description='Genres operations')

@ns.route('/')
class Genres(Resource):
    @ns.doc('List all genres')
    def get(self):
        return jsonify([
            {"id": 1, "name": "Mystery"},
            {"id": 2, "name": "Crime"}
        ])
