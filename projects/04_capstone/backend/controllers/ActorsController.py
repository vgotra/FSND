import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from auth.AuthService import requires_auth
from schemas.ActorSchema import ActorSchema
from schemas.ActorsSchema import ActorsSchema
from flask import request
from flask_restx import Resource
from models.ActorModels import ns, actor_get, actor_put, actors_get
from app import db
from data_access.repositories.ActorsRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class ActorsController(Resource):
    @ns.response(200, "Success", model=actors_get)
    def get(self):
        actors = ActorsRepository(db).get_all()
        return ActorsSchema().dump(actors)

    @requires_auth("put:actor")
    @ns.expect(actor_put)
    @ns.response(200, "Success", model=actor_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        print(json_data)
        actor = ActorSchema().load(json_data)
        actor_db = ActorsRepository(db).create(actor)
        return ActorSchema().dump(actor_db)
