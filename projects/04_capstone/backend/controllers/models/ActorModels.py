from flask_restx import Namespace, fields

ns = Namespace("actors", description="Actors operations")

actor_get = ns.model("Actor Get", {"id": fields.Integer, "name": fields.String, "birthday": fields.Date, "sex": fields.String, "profileUrl": fields.Url, "photoUrl": fields.Url})

actors_get = ns.model("Actors Get", {"actors": fields.List(fields.Nested(actor_get)), "page": fields.Integer, "pages": fields.Integer, "total": fields.Integer})

actor_put = ns.model("Actor Put", {"name": fields.String, "birthday": fields.Date, "sex": fields.String, "profileUrl": fields.Url, "photoUrl": fields.Url})

actor_patch = ns.model("Actor Patch", {"id": fields.Integer, "name": fields.String, "birthday": fields.Date, "sex": fields.String, "profileUrl": fields.Url, "photoUrl": fields.Url})
