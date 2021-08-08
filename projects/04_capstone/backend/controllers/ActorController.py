import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from schemas.ActorSchema import ActorSchema
from flask import request
from flask_restx import Resource
from models.ActorModels import ns, actor_get, actor_patch
from app import db
from data_access.repositories.ActorsRepository import *


@ns.route("/<int:id>")
@ns.doc(params={"id": "Actor id"})
@ns.response(401, "Authentication Error")
class ActorController(Resource):
    @ns.response(200, "Success", model=actor_get)
    def get(self, id):
        actor = ActorsRepository(db).get(id)
        return ActorSchema().dump(actor)

    @ns.expect(actor_patch)
    @ns.response(200, "Success", model=actor_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        actor = ActorSchema().load(json_data)
        return ActorSchema().dump(actor)

    def delete(self, id):
        pass
