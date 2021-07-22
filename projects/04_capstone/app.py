from flask import Flask
from blueprints.Movies import movies
from blueprints.Actors import actors

app = Flask(__name__)
app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(actors, url_prefix='/actors')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()
