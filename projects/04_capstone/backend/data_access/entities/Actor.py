from data_access import db


class Actor(db.Model):
    __tablename__ = "Actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birthday = db.Column(db.Datetime)
    sex = db.Column(db.Boolean)
    profile_url = db.Column(db.String(300))
    photo_url = db.Column(db.String(300))
