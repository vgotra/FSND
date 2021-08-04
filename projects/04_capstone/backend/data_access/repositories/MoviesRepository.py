from data_access.entities.Movie import Movie


class MoviesRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, search_phrase):
        movies_query = self.db.session.query(Movie).order_by(Movie.id)
        if search_phrase:
            movies_query = movies_query.filter(Movie.name.ilike("%{}%".format(search_phrase)))
        count = movies_query.count()
        movies = movies_query.all()
        return (count, movies)

    def get(self, id):
        movie = self.db.session.query(Movie).filter(Movie.id == id).first()
        return movie

    def update(self, id, movie):
        movie_db = self.db.session.query(Movie).filter(Movie.id == id).first()
        self.set_data(movie_db, movie)
        self.db.session.commit()

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
