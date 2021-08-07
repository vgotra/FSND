from data_access import db


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    profile_url = db.Column(db.String(300))
    photo_url = db.Column(db.String(300))
