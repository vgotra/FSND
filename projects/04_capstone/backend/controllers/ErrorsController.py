import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app
from flask import jsonify
from auth.AuthError import AuthError
from common.models.ApiError import ApiError
from marshmallow.exceptions import ValidationError


@app.errorhandler(ValidationError)
def auth_error(error):
    return jsonify({"success": False, "error": 400, "message": error.normalized_messages()}), 400


@app.errorhandler(ApiError)
def api_error(error):
    return jsonify({"success": False, "error": error.status_code, "message": error.error}), error.status_code


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({"success": False, "error": error.status_code, "message": error.error}), error.status_code


@app.errorhandler(Exception)
def server_error(error):
    print(error)
    return jsonify({"success": False, "error": 500, "message": "server error"}), 500
