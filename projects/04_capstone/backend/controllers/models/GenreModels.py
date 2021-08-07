from flask_restplus import Resource, Namespace, fields

ns = Namespace("genres", description="Genres operations")

genre_get = ns.model("Genre Get", {"id": fields.Integer, "name": fields.String})

genre_put = ns.model("Genre Put", {"name": fields.String})

genre_patch = ns.model("Genre Patch", {"id": fields.Integer, "name": fields.String})
