from flask import request, jsonify
import random

from app import app
from data_access.database_models import Question


@app.route('/api/quizzes', methods=['POST'])
def quizzes_get_all():
    request_json = request.get_json()
    previous_questions = request_json['previous_questions']
    quiz_category_id = request_json['quiz_category']['id']
    questions_in_db = []
    if quiz_category_id > 0:
        questions_in_db = Question.query.filter(
            Question.category == quiz_category_id).all()
    else:
        questions_in_db = Question.query.all()
    random_int = random.randint(0, len(questions_in_db) - 1)
    question_in_db = questions_in_db[random_int]
    while question_in_db.id in previous_questions:
        random_int = random.randint(0, len(questions_in_db) - 1)
        question_in_db = questions_in_db[random_int]
    question = question_in_db.format()
    return jsonify({'question': question})
