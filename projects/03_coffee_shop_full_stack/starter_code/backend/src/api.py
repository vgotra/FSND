from flask import Flask
from sqlalchemy import exc


from data_access.models import setup_db
# from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)

#db_drop_and_create_all()

from controllers.DrinksController import *
from controllers.AppController import *

if __name__ == '__main__':
    app.run()