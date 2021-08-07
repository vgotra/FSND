import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.LanguageSchema import LanguageSchema
from flask import request
from flask_restx import Resource
from models.LanguageModels import ns, language_get, language_patch


@ns.route("/<int:id>")
@ns.doc(params={"id": "Language id"})
@ns.response(401, "Authentication Error")
class LanguagesController(Resource):
    @ns.response(200, "Success", model=language_get)
    def get(self, id):
        language = {"id": 1, "name": "Ukrainian"}
        return LanguageSchema().dump(language)

    @ns.expect(language_patch)
    @ns.response(200, "Success", model=language_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        language = LanguageSchema().load(json_data)  # Add validation error
        print("languages/patch:")
        print(language)
        pass

    def delete(self, id):
        pass
