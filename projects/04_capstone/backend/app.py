import os
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restx import Api
from flask import Flask, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from data_access import db

from controllers.MoviesController import ns as MoviesController
from controllers.MovieController import ns as MovieController
from controllers.ActorsController import ns as ActorsController
from controllers.ActorController import ns as ActorController
from controllers.GenresController import ns as GenresController
from controllers.GenreController import ns as GenreController
from controllers.LanguagesController import ns as LanguagesController
from controllers.LanguageController import ns as LanguageController

from data_access.entities import *

authorizations = {"Bearer Auth": {"type": "apiKey", "in": "header", "name": "Authorization"}}

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

CORS(app)

api = Api(app, version="1.0", title="Capstone Agency API", description="A Capstone Agency API", prefix="/api", doc="/docs", security="Bearer Auth", authorizations=authorizations)

api.add_namespace(MoviesController)
api.add_namespace(MovieController)
api.add_namespace(ActorsController)
api.add_namespace(ActorController)
api.add_namespace(GenresController)
api.add_namespace(GenreController)
api.add_namespace(LanguagesController)
api.add_namespace(LanguageController)


@app.route("/", defaults={"route": None})
@app.route("/<route>")
def index(route):
    if route:
        return render_template("index.html", route=route)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
