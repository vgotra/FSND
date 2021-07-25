from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('actors', description='Actors operations')

@ns.route('/<int:id>')
class Actor(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "Kevin Spacey"})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass