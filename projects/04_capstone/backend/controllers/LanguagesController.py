from flask import jsonify
from flask_restplus import Resource, Namespace

ns = Namespace("languages", description="Languages operations")


@ns.route("/")
class LanguagesController(Resource):
    @ns.doc("List all languages")
    def get(self):
        return jsonify([{"id": 1, "name": "Ukrainian"}, {"id": 2, "name": "English"}])

    def put(self):
        pass
