import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api
from flask import Flask
from controllers.Movies import ns as Movies
from controllers.Movie import ns as Movie
from controllers.Actors import ns as Actors
from controllers.Actor import ns as Actor

app = Flask(__name__)

api = Api(app, version='1.0', title='Capstone Agency API',
    description='A Capstone Agency API',
)

api.add_namespace(Movies)
api.add_namespace(Movie)
api.add_namespace(Actors)
api.add_namespace(Actor)

if __name__ == '__main__':
    app.run()
