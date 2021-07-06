import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from data_access.database_models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setup_db_for_test(self):
        self.db_username = os.getenv('TRIVIA_DB_USERNAME')
        self.db_password = os.getenv('TRIVIA_DB_PASSWORD')
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            self.db_username, self.db_password, 'localhost:5432', self.database_name)

    def create_test_entities(self):
        category = Category("Category")
        category.insert()
        question = Question("Question", "Answer", 1, 1)
        question.insert()

    def setUp(self):
        """Define test variables and initialize app."""
        app.config.from_mapping(DEBUG=False, TESTING=True)
        self.app = app
        self.client = self.app.test_client
        self.setup_db_for_test()
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            Question.__table__.drop(self.db.engine)
            Category.__table__.drop(self.db.engine)
            setup_db(self.app, self.database_path)
            # create some test entities
            self.create_test_entities()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_categories_all_success(self):
        """Test: Get all categories - Success"""
        res = self.client().get('/api/categories')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json, {'categories': [{'id': 1, 'type': 'Category'}]})

    def test_category_questions_by_category_id(self):
        """Test: Get questions by category id - Success"""
        res = self.client().get('/api/categories/1/questions')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json,
                         {'current_category': {'id': 1,
                          'type': 'Category'},
                          'questions': [{'answer': 'Answer',
                                         'category': 1,
                                         'difficulty': 1,
                                         'id': 1,
                                         'question': 'Question'}],
                             'total_questions': 1})

    def test_questions_all(self):
        """Test: Get all questions - Success"""
        res = self.client().get('/api/questions/1')  # TODO Add 405 error
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json,
                         {'categories': [{'id': 1,
                                          'type': 'Category'}],
                          'current_category': {},
                          'questions': [{'answer': 'Answer',
                                         'category': 1,
                                         'difficulty': 1,
                                         'id': 1,
                                         'question': 'Question'}],
                             'total_questions': 1})

    def test_questions_search(self):
        """Test: Search questions - Success"""
        res = self.client().get('/api/questions/search/question')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json,
                         {'current_category': {},
                          'questions': [{'answer': 'Answer',
                                         'category': 1,
                                         'difficulty': 1,
                                         'id': 1,
                                         'question': 'Question'}],
                             'total_questions': 1})

    def test_questions_add(self):
        """Test: Add question - Success"""
        res = self.client().post('/api/questions',
                                 data=json.dumps(dict({'question': 'Question',
                                                       'answer': 'Answer',
                                                       'category': 1,
                                                       'difficulty': 1})),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, {'success': True})

    def test_questions_delete_by_id(self):
        """Test: Delete question by id - Success"""
        res = self.client().delete('/api/questions/2')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, {'success': True})

    def test_quizzes(self):
        """Test: Get quizzes - Success"""
        res = self.client().post('/api/quizzes',
                                 data=json.dumps(dict({'previous_questions': [],
                                                       'quiz_category': {'id': 1}})),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json, {'question': {
                         'answer': 'Answer', 'category': 1, 'difficulty': 1, 'id': 1, 'question': 'Question'}})


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
