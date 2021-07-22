from flask import Blueprint, jsonify

movies = Blueprint('movies', __name__)


@movies.route('/')
def get_all():
    return jsonify([
        {"id": 1, "name": "The Usual Suspects"},
        {"id": 2, "name": "The Matrix"}
    ])


@movies.route('/<id>')
def get_by_id(id):
    return jsonify({"id": 1, "name": "The Usual Suspects"})
