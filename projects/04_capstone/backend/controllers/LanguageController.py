import os
import sys

from flask.json import jsonify

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.LanguageSchema import LanguageSchema
from flask import request
from flask_restx import Resource
from models.LanguageModels import ns, language_get, language_patch
from app import db
from data_access.repositories.LanguagesRepository import *
from common.exceptions.ApiError import ApiError


@ns.route("/<int:id>")
@ns.doc(params={"id": "Language id"})
@ns.response(401, "Authentication Error")
@ns.response(404, "Not Found")
class LanguagesController(Resource):
    @requires_auth("get:language-details")
    @ns.response(200, "Success", model=language_get)
    def get(self, id):
        language = LanguagesRepository(db).get(id)
        if not language:
            raise ApiError("Language is not found", 404)
        return LanguageSchema().dump(language)

    @requires_auth("patch:language")
    @ns.expect(language_patch)
    @ns.response(200, "Success", model=language_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        language = LanguageSchema().load(json_data)
        try:
            language_db = LanguagesRepository(db).update(id, language)
            return LanguageSchema().dump(language_db)
        except NotFound:
            raise ApiError("Language is not found", 404)

    @requires_auth("delete:language")
    def delete(self, id):
        try:
            deleted_id = LanguagesRepository(db).delete(id)
            return jsonify({"id": deleted_id})
        except NotFound:
            raise ApiError("Language is not found", 404)
