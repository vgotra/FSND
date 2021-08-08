from flask_restx import Namespace, fields

ns = Namespace("languages", description="Languages operations")

language_get = ns.model("Language Get", {"id": fields.Integer, "name": fields.String})

languages_get = ns.model("Languages Get", {"languages": fields.List(fields.Nested(language_get)), "page": fields.Integer, "pages": fields.Integer, "total": fields.Integer})

language_put = ns.model("Language Put", {"name": fields.String})

language_patch = ns.model("Language Patch", {"id": fields.Integer, "name": fields.String})
