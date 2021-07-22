from data_access import db


class Movie(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    release_country = db.Column(db.String(50))
