from flask_restplus import Resource, Namespace, fields

ns = Namespace("movies", description="Movies operations")

movie_get = ns.model("Movie Get", {"id": fields.Integer, "name": fields.String})

movie_put = ns.model("Movie Put", {"name": fields.String})

movie_patch = ns.model("Movie Patch", {"id": fields.Integer, "name": fields.String})
