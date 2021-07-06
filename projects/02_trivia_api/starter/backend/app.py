import logging
from flask import Flask
from database_models import setup_db

app = Flask(__name__)
setup_db(app)

from controllers.AppController import *
from controllers.CategoriesController import *
from controllers.QuestionsController import *
from controllers.QuizzesController import *

if not app.debug:
    app.logger.setLevel(logging.INFO)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()
