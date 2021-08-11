from data_access.entities.Movie import Movie
from data_access.exceptions.NotFound import NotFound


class MoviesRepository:
    def __init__(self, db):
        self.db = db
        self.per_page = 10

    def get_all(self, page=1, search_phrase=None):
        movies_query = self.db.session.query(Movie).order_by(Movie.id)
        if search_phrase:
            movies_query = movies_query.filter(Movie.name.ilike("%{}%".format(search_phrase)))
        movies = movies_query.paginate(page, self.per_page, error_out=False)
        return movies

    def get(self, id):
        movie = self.db.session.query(Movie).filter(Movie.id == id).first()
        return movie

    def update(self, id, movie):
        movie_db = self.db.session.query(Movie).filter(Movie.id == id).first()
        if not movie_db:
            raise NotFound("Entity is not found")
        self.set_data(movie_db, movie)
        self.db.session.commit()
        return movie_db

    def create(self, movie):
        new_movie = Movie()
        self.set_data(new_movie, movie)
        self.db.session.add(new_movie)
        self.db.session.commit()
        return new_movie

    def delete(self, id):
        movie_db = self.db.session.query(Movie).filter(Movie.id == id).first()
        if not movie_db:
            raise NotFound("Entity is not found")
        self.db.session.delete(movie_db)
        self.db.session.commit()
        return id

    def set_data(self, movie_db, movie_model):
        movie_db.name = movie_model['name']
        movie_db.description = movie_model['description']
        movie_db.release_date = movie_model['release_date']
        movie_db.release_country = movie_model['release_country']

