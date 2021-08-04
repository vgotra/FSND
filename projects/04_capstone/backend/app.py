import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api
from flask import Flask, render_template
from flask_cors import CORS

from controllers.MoviesController import ns as MoviesController
from controllers.MovieController import ns as MovieController
from controllers.ActorsController import ns as ActorsController
from controllers.ActorController import ns as ActorController
from controllers.GenresController import ns as GenresController
from controllers.GenreController import ns as GenreController
from controllers.LanguagesController import ns as LanguagesController
from controllers.LanguageController import ns as LanguageController


app = Flask(__name__)
CORS(app)
api = Api(app, version="1.0", title="Capstone Agency API", description="A Capstone Agency API", prefix="/api", doc="/docs")

api.add_namespace(MoviesController)
api.add_namespace(MovieController)
api.add_namespace(ActorsController)
api.add_namespace(ActorController)
api.add_namespace(GenresController)
api.add_namespace(GenreController)
api.add_namespace(LanguagesController)
api.add_namespace(LanguageController)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
