from data_access.entities.Genre import Genre


class GenresRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, search_phrase):
        genres_query = self.db.session.query(Genre).order_by(Genre.id)
        if search_phrase:
            genres_query = genres_query.filter(Genre.name.ilike("%{}%".format(search_phrase)))
        count = genres_query.count()
        genres = genres_query.all()
        return (count, genres)

    def get(self, id):
        genre = self.db.session.query(Genre).filter(Genre.id == id).first()
        return genre

    def update(self, id, genre):
        genre_db = self.db.session.query(Genre).filter(Genre.id == id).first()
        self.set_data(genre_db, genre)
        self.db.session.commit()

    def create(self, genre):
        new_genre = Genre()
        self.set_data(new_genre, genre)
        self.db.session.add(new_genre)
        self.db.session.commit()

    def set_data(genre_db, genre_model):
        genre_db.name = genre_model.name
        genre_db.phone = genre_model.birthday
        genre_db.sex = genre_model.sex
        genre_db.profile_url = genre_model.profile_url
        genre_db.photo_url = genre_model.photo_url
