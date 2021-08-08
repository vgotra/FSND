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

    def set_data(movie_db, movie_model):
        movie_db.name = movie_model.name
        movie_db.phone = movie_model.birthday
        movie_db.sex = movie_model.sex
        movie_db.profile_url = movie_model.profile_url
        movie_db.photo_url = movie_model.photo_url
