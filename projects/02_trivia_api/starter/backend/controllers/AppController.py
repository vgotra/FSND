from flask import jsonify, render_template
from flask_cors import CORS

from app import app


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

@app.route('/docs')
def docs():
    return render_template('index.html')

@app.errorhandler(400)
def bad_request(error):
    return jsonify({ "success": False, "error": 400, "message": "Bad request" }), 400

@app.errorhandler(401)
def bad_request(error):
    return jsonify({ "success": False, "error": 401, "message": "Unauthorized" }), 401

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({ "success": False, "error": 404, "message": "Not found" }), 404

@app.errorhandler(422)
def unprocessable_entity_error(error):
    return jsonify({ "success": False, "error": 422, "message": "Unprocessable entity" }), 422

@app.errorhandler(500)
def server_error(error):
    return jsonify({ "success": False, "error": 500, "message": "Server error" }), 500
