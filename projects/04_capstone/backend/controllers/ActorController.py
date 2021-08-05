import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.schemas.ActorSchema import ActorSchema
from flask_restplus import Resource, Namespace
from datetime import datetime

ns = Namespace("actors", description="Actors operations")


@ns.route("/<int:id>")
class ActorController(Resource):
    def get(self, id):
        actor = {"id": 1, "name": "Kevin Spacey", "birthday": datetime.strptime("Jul 26 1959", "%b %d %Y"), "sex": "Male", "profile_url": "", "photo_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjDIrdmcEsDYWAq_O9AC0799hKpHNLfWULqeBPM5jssX7AQ_Ee"}
        return ActorSchema().dump(actor)

    def patch(self, id):
        pass

    def delete(self, id):
        pass
