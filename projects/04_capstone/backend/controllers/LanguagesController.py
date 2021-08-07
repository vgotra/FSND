import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.LanguageSchema import LanguageSchema
from flask import request
from flask_restx import Resource
from models.LanguageModels import ns, language_get, language_put


@ns.route("/")
@ns.response(401, "Authentication Error")
class LanguagesController(Resource):
    @ns.response(200, "Success", model=[language_get])
    def get(self):
        languages = [{"id": 1, "name": "Ukrainian"}, {"id": 2, "name": "English"}]
        return LanguageSchema().dump(languages, many=True)

    @ns.expect(language_put)
    @ns.response(200, "Success", model=language_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        languages = LanguageSchema().load(json_data)  # Add validation error
        print("languages/put:")
        print(languages)
