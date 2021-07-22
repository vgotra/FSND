from data_access import db


class Genre(db.Model):
    __tablename__ = 'Genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
