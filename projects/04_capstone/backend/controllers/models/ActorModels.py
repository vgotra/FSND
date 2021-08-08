from flask_restx import Namespace, fields

ns = Namespace("actors", description="Actors operations")

actor_get = ns.model("Actor Get", {"id": fields.Integer, "name": fields.String})

actor_put = ns.model("Actor Put", {"name": fields.String})

actor_patch = ns.model("Actor Patch", {"id": fields.Integer, "name": fields.String})
