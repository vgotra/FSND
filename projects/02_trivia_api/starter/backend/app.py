import logging
from flask import Flask
from data_access.database_models import setup_db

app = Flask(__name__)
setup_db(app)

from controllers.QuizzesController import *
from controllers.QuestionsController import *
from controllers.CategoriesController import *
from controllers.AppController import *

if not app.debug:
    app.logger.setLevel(logging.INFO)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()
