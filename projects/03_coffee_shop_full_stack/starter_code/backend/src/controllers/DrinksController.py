import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, abort

from api import app
from data_access.models import db_drop_and_create_all, setup_db, Drink
from services.auth import requires_auth

@app.route('/drinks', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_get():
    drinks = [drunk.short() for drunk in Drink.query.all()]
    return jsonify({"success": True, "drinks": drinks})

@app.route('/drinks-detail', methods=['GET'])
def drinks_get_detail():
    drinks = [drunk.long() for drunk in Drink.query.all()]
    return jsonify({"success": True, "drinks": drinks})

@app.route('/drinks', methods=['POST'])
def drinks_create():
    drinks = [drunk.short() for drunk in Drink.query.all()]
    return jsonify({"success": True, "drinks": drinks[0]}) # TODO returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['PATCH'])
def drinks_update(id):
    pass


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
def drinks_delete(id):
    pass