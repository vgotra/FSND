from flask import jsonify
from flask_restplus import Resource, Namespace
from datetime import datetime

ns = Namespace('actors', description='Actors operations')

@ns.route('/')
class Actors(Resource):
    def get(self):
        return jsonify([
            {"id": 1, "name": "Kevin Spacey", "birthday": datetime.strptime('Jul 26 1959', "%b %d %Y"), "sex": "Male", "profileUrl": "", "photoUrl": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjDIrdmcEsDYWAq_O9AC0799hKpHNLfWULqeBPM5jssX7AQ_Ee"},
            {"id": 2, "name": "Keanu Reeves", "birthday": datetime.strptime('Sep 2 1964', "%b %d %Y"), "sex": "Male", "profileUrl": "", "photoUrl": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTkqugX0WLc78TSUXjzYAQvwT7nqU8vJknuJGldrNv0FO7kD8vl"}
        ])

    def put(self):
        pass
