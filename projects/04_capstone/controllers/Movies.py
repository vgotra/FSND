from flask import jsonify
from flask_restplus import Resource, Namespace, fields

ns = Namespace('movies', description='Movies operations')

@ns.route('/')
class Movies(Resource):
    @ns.doc('List all movies')
    def get(self):
        return jsonify([
            {"id": 1, "name": "The Usual Suspects"},
            {"id": 2, "name": "The Matrix"}
        ])
