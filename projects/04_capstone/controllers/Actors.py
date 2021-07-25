from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('actors', description='Actors operations')

@ns.route('/')
class Actors(Resource):
    def get(self):
        return jsonify([
            {"id": 1, "name": "Kevin Spacey"},
            {"id": 2, "name": "Keanu Reeves"}
        ])
