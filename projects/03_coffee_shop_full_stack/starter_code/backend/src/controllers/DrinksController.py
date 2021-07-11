import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from services.AuthService import requires_auth
from data_access.DatabaseModels import Drink
from api import app
from flask import request, jsonify
from errors.ApiError import ApiError


@app.route('/api/drinks', methods=['GET'])
def drinks_get():
    drinks = [drunk.short() for drunk in Drink.query.all()]
    return jsonify({"success": True, "drinks": drinks}), 200


@app.route('/api/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_get_detail():
    drinks = [drunk.long() for drunk in Drink.query.all()]
    return jsonify({"success": True, "drinks": drinks}), 200


@app.route('/api/drinks', methods=['POST'])
@requires_auth('post:drinks')
def drinks_create():
    request_json = request.get_json()
    title = request_json['title']
    drink = Drink(title=title)
    if request_json.get('recipe'):
        recipe = request_json['recipe']
        if not (isinstance(recipe, list)):
            raise ApiError("Recipe should be array of recipes", 400)
        drink = Drink(title=title, recipe=str(recipe).replace("\'", "\""))
    drink.insert()
    return jsonify({"success": True, "drink": drink.long()}), 201


@app.route('/api/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def drinks_update(id):
    drink = Drink.query.filter(Drink.id == id).first()
    if not (drink):
        raise ApiError("Drink is not found", 404)
    request_json = request.get_json()
    title = request_json['title']
    drink.title = title
    if request_json.get('recipe'):
        recipe = request_json['recipe']
        if not (isinstance(recipe, list)):
            raise ApiError("Recipe should be array of recipes", 400)
        drink.recipe = str(recipe).replace("\'", "\"")
    drink.update()
    return jsonify({"success": True, "drink": drink.long()}), 200


@app.route('/api/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def drinks_delete(id):
    drink = Drink.query.filter(Drink.id == id).first()
    if not (drink):
        raise ApiError("Drink is not found", 404)
    drink.delete()
    return jsonify({"success": True, "id": id}), 200
