import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from schemas.ActorSchema import ActorSchema
from schemas.ActorsSchema import ActorsSchema
from flask import request
from flask_restx import Resource
from models.ActorModels import ns, actor_get, actor_put
from app import db
from data_access.repositories.ActorsRepository import *


@ns.route("/")
@ns.response(401, "Authentication Error")
class ActorsController(Resource):
    @ns.response(200, "Success", model=[actor_get])
    def get(self):
        actors = ActorsRepository(db).get_all()
        # actors = [
        #     {"id": 1, "name": "Kevin Spacey", "birthday": datetime.strptime("Jul 26 1959", "%b %d %Y"), "sex": "Male", "profile_url": "", "photo_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjDIrdmcEsDYWAq_O9AC0799hKpHNLfWULqeBPM5jssX7AQ_Ee"},
        #     {"id": 2, "name": "Keanu Reeves", "birthday": datetime.strptime("Sep 2 1964", "%b %d %Y"), "sex": "Male", "profile_url": "", "photo_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTkqugX0WLc78TSUXjzYAQvwT7nqU8vJknuJGldrNv0FO7kD8vl"},
        # ]
        return ActorsSchema().dump(actors)

    @ns.expect(actor_put)
    @ns.response(200, "Success", model=actor_get)
    @ns.response(400, "Bad Request")
    def put(self):
        json_data = request.get_json()
        actor = ActorSchema().load(json_data)
        print("actors/put:")
        print(actor)
        return ActorSchema().dump(actor)
