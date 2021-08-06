import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.LanguageSchema import LanguageSchema
from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime

ns = Namespace("languages", description="Languages operations")


@ns.route("/<int:id>")
@ns.doc(params={'id': 'Language id'})
class LanguagesController(Resource):
    def get(self, id):
        language = {"id": 1, "name": "Ukrainian"}
        return LanguageSchema().dump(language)

    def patch(self, id):
        json_data = request.get_json()
        language = LanguageSchema().load(json_data) # Add validation error
        print("languages/patch:")
        print(language)
        pass

    def delete(self, id):
        pass
