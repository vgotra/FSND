import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.ActorSchema import ActorSchema
from flask import request
from flask_restx import Resource
from datetime import datetime
from models.ActorModels import ns, actor_get, actor_patch


@ns.route("/<int:id>")
@ns.doc(params={"id": "Actor id"})
@ns.response(401, "Authentication Error")
class ActorController(Resource):
    @ns.response(200, "Success", model=actor_get)
    def get(self, id):
        actor = {"id": 1, "name": "Kevin Spacey", "birthday": datetime.strptime("Jul 26 1959", "%b %d %Y"), "sex": "Male", "profile_url": "", "photo_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjDIrdmcEsDYWAq_O9AC0799hKpHNLfWULqeBPM5jssX7AQ_Ee"}
        return ActorSchema().dump(actor)

    @ns.expect(actor_patch)
    @ns.response(200, "Success", model=actor_get)
    @ns.response(400, "Bad Request")
    def patch(self, id):
        json_data = request.get_json()
        actor = ActorSchema().load(json_data)  # Add validation error
        print("actors/patch:")
        print(actor)

    def delete(self, id):
        pass
