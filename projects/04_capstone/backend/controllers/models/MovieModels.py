from flask_restx import Namespace, fields

ns = Namespace("movies", description="Movies operations")

movie_get = ns.model("Movie Get", {"id": fields.Integer, "name": fields.String, "description": fields.String, "releaseDate": fields.Date, "releaseCountry": fields.String})

movies_get = ns.model("Movies Get", {"movies": fields.List(fields.Nested(movie_get)), "page": fields.Integer, "pages": fields.Integer, "total": fields.Integer})

movie_put = ns.model("Movie Put", {"name": fields.String, "description": fields.String, "releaseDate": fields.Date, "releaseCountry": fields.String})

movie_patch = ns.model("Movie Patch", {"id": fields.Integer, "name": fields.String, "description": fields.String, "releaseDate": fields.Date, "releaseCountry": fields.String})

movie_delete = ns.model("Movie Delete", {"id": fields.Integer})
