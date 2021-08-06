import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.LanguageSchema import LanguageSchema
from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime

ns = Namespace("languages", description="Languages operations")


@ns.route("/")
class LanguagesController(Resource):
    @ns.doc("List all languages")
    def get(self):
        languages = [{"id": 1, "name": "Ukrainian"}, {"id": 2, "name": "English"}]
        return LanguageSchema().dump(languages, many=True)

    def put(self):
        json_data = request.get_json()
        languages = LanguageSchema().load(json_data) # Add validation error
        print("languages/put:")
        print(languages)
        pass
