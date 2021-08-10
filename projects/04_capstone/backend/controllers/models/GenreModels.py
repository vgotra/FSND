from flask_restx import Namespace, fields

ns = Namespace("genres", description="Genres operations")

genre_get = ns.model("Genre Get", {"id": fields.Integer, "name": fields.String})

genres_get = ns.model("Genres Get", {"genres": fields.List(fields.Nested(genre_get)), "page": fields.Integer, "pages": fields.Integer, "total": fields.Integer})

genre_put = ns.model("Genre Put", {"name": fields.String})

genre_patch = ns.model("Genre Patch", {"id": fields.Integer, "name": fields.String})

genre_delete = ns.model("Genre Delete", {"id": fields.Integer})
