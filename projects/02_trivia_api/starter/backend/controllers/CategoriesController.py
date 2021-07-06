from flask import jsonify

from app import app
from data_access.database_models import Question, Category


@app.route('/api/categories', methods=['GET'])
def categories_get_all():
    all_categories_in_db = Category.query.all()
    all_categories = [category.format() for category in all_categories_in_db]
    return jsonify({'categories': all_categories})


@app.route('/api/categories/<int:id>/questions', methods=['GET'])
def categories_get_questions_by_category_id(id):
    category = Category.query.filter(Category.id == id).first().format()
    questions_in_db = Question.query.filter(Question.category == id).all()
    all_questions = [question.format() for question in questions_in_db]
    return jsonify({'total_questions': len(all_questions),
                   'questions': all_questions, 'current_category': category})
