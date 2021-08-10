import os
import sys

from flask.json import jsonify

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.ActorSchema import ActorSchema
from flask import request
from flask_restx import Resource, model
from models.ActorModels import ns, actor_get, actor_patch, actor_delete
from app import db
from data_access.repositories.ActorsRepository import *
from common.exceptions.ApiError import ApiError


@ns.route("/<int:id>")
@ns.doc(params={"id": "Actor id"})
@ns.response(401, "Authentication Error")
@ns.response(404, "Not Found")
class ActorController(Resource):
    @requires_auth("get:actor-details")
    @ns.response(200, "Success", model=actor_get)
    def get(self, id):
        actor = ActorsRepository(db).get(id)
        if not actor:
            raise ApiError("Actor is not found", 404)
        return ActorSchema().dump(actor)

    @requires_auth("patch:actor")
    @ns.expect(actor_patch)
    @ns.response(200, "Success", model=actor_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        actor = ActorSchema().load(json_data)
        try:
            actor_db = ActorsRepository(db).update(id, actor)
            return ActorSchema().dump(actor_db)
        except NotFound:
            raise ApiError("Actor is not found", 404)

    @requires_auth("delete:actor")
    @ns.response(200, "Success", model=actor_delete)
    def delete(self, id):
        try:
            deleted_id = ActorsRepository(db).delete(id)
            return jsonify({"id": deleted_id})
        except NotFound:
            raise ApiError("Actor is not found", 404)
