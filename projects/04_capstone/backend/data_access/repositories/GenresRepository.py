from data_access.entities.Genre import Genre
from data_access.exceptions.NotFound import NotFound


class GenresRepository:
    def __init__(self, db):
        self.db = db
        self.per_page = 10

    def get_all(self, page=1, search_phrase=None):
        genres_query = self.db.session.query(Genre).order_by(Genre.id)
        if search_phrase:
            genres_query = genres_query.filter(Genre.name.ilike("%{}%".format(search_phrase)))
        genres = genres_query.paginate(page, self.per_page, error_out=False)
        return genres

    def get(self, id):
        genre = self.db.session.query(Genre).filter(Genre.id == id).first()
        return genre

    def update(self, id, genre):
        genre_db = self.db.session.query(Genre).filter(Genre.id == id).first()
        if not genre_db:
            raise NotFound("Entity is not found")
        self.set_data(genre_db, genre)
        self.db.session.commit()
        return genre_db

    def create(self, genre):
        new_genre = Genre()
        self.set_data(new_genre, genre)
        self.db.session.add(new_genre)
        self.db.session.commit()
        return new_genre

    def delete(self, id):
        genre_db = self.db.session.query(Genre).filter(Genre.id == id).first()
        if not genre_db:
            raise NotFound("Entity is not found")
        self.db.session.delete(genre_db)
        self.db.session.commit()
        return id

    def set_data(genre_db, genre_model):
        genre_db.name = genre_model.name
        genre_db.phone = genre_model.birthday
        genre_db.sex = genre_model.sex
        genre_db.profile_url = genre_model.profile_url
        genre_db.photo_url = genre_model.photo_url
