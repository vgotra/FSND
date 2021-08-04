from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace("languages", description="Languages operations")


@ns.route("/<int:id>")
class LanguagesController(Resource):
    def get(self, id):
        return jsonify({"id": 1, "name": "Ukrainian"})

    def patch(self, id):
        pass

    def delete(self, id):
        pass
