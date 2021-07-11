from flask import Flask
from data_access.DatabaseModels import db_drop_and_create_all, setup_db


app = Flask(__name__)
setup_db(app)

# Uncomment if you need to create new database
# db_drop_and_create_all()

from controllers.DrinksController import *
from controllers.AppController import *

if __name__ == '__main__':
    app.run()
