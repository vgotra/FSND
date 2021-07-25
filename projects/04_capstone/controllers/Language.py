from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace('languages', description='Languages operations')

@ns.route('/<int:id>')
class Languages(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "Ukrainian"})

    def post(self, id):
        pass

    def delete(self, id):
        pass