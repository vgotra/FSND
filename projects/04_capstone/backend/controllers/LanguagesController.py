import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from schemas.LanguageSchema import LanguageSchema
from schemas.LanguagesSchema import LanguagesSchema
from flask import request
from flask_restx import Resource
from models.LanguageModels import ns, language_get, language_put
from app import db
from data_access.repositories.LanguagesRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class LanguagesController(Resource):
    @ns.response(200, "Success", model=[language_get])
    def get(self):
        languages = LanguagesRepository(db).get_all()
        return LanguagesSchema().dump(languages)

    @ns.expect(language_put)
    @ns.response(200, "Success", model=language_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        language = LanguageSchema().load(json_data)
        return LanguageSchema().dump(language)
