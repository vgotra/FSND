import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from api import app
from flask_cors import CORS
from flask import jsonify
from errors.AuthError import AuthError
from errors.ApiError import ApiError


cors = CORS(app)

@app.errorhandler(ApiError)
def api_error(error):
    return jsonify({"success": False, "error": error.status_code,
                   "message": error.error}), error.status_code


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({"success": False, "error": error.status_code,
                   "message": error.error}), error.status_code


@app.errorhandler(Exception)
def server_error(error):
    print(error)
    return jsonify({"success": False, "error": 500,
                   "message": "server error"}), 500
