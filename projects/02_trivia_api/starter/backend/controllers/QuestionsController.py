from flask import request, jsonify

from app import app
from database_models import Question, Category

QUESTIONS_PER_PAGE = 10

@app.route('/api/questions/<int:page>', methods=['GET'])
def questions_get_all(page):
    query = Question.query
    total = query.count()
    if page <= 1:
        query = query.limit(QUESTIONS_PER_PAGE)
    else:
        query = query.limit(QUESTIONS_PER_PAGE).offset(QUESTIONS_PER_PAGE * (page - 1))
    all_questions_in_db = query.all()
    all_questions = [question.format() for question in all_questions_in_db]
    all_categories_in_db = Category.query.all()
    all_categories = [category.format() for category in all_categories_in_db]
    return jsonify({"total_questions": total, "questions": all_questions, "current_category": {}, "categories": all_categories})

@app.route('/api/questions/search/<search_term>', methods=['GET'])
def questions_search(search_term):
    all_questions_in_db = Question.query.filter(Question.question.ilike("%{}%".format(search_term))).all() 
    all_questions = [question.format() for question in all_questions_in_db]
    return jsonify({"total_questions": len(all_questions_in_db), "questions": all_questions, "current_category": {}}) #TODO Add category

@app.route('/api/questions', methods=['POST'])
def questions_create():
    request_json = request.get_json()
    question = request_json['question']
    answer = request_json['answer']
    category = request_json['category']
    difficulty = request_json['difficulty']
    question = Question(question, answer, category, difficulty)
    #TODO Add try catch finally 
    question.insert()
    return jsonify({"success": True})

@app.route('/api/questions/<int:id>', methods=['DELETE'])
def questions_delete(id):
    question = Question.query.filter(Question.id == id).first()
    if question:
        #TODO Add try catch finally
        question.delete() 
    return jsonify({"success": True})
