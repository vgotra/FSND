from data_access import db


class Language(db.Model):
    __tablename__ = 'Languages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
