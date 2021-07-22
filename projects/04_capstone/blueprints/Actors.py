from flask import Blueprint, jsonify

actors = Blueprint('actors', __name__)


@actors.route('/')
def get_all():
    return jsonify([
        {"id": 1, "name": "Kevin Spacey"},
        {"id": 2, "name": "Keanu Reeves"}
    ])


@actors.route('/<id>')
def get_by_id(id):
    return jsonify({"id": 1, "name": "Kevin Spacey"})
