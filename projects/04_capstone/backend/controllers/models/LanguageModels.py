from flask_restx import Resource, Namespace, fields

ns = Namespace("languages", description="Languages operations")

language_get = ns.model("Language Get", {"id": fields.Integer, "name": fields.String})

language_put = ns.model("Language Put", {"name": fields.String})

language_patch = ns.model("Language Patch", {"id": fields.Integer, "name": fields.String})
