import logging
import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://fyyur:fyyur123!@localhost/fyyur'

SQLALCHEMY_TRACK_MODIFICATIONS = False

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)