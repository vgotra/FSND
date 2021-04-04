from data_access import db


class Show(db.Model):
    __tablename__ = 'Shows'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venues.id'), nullable=False)
    venue = db.relationship('Venue', back_populates='shows', lazy='joined')
    artist_id = db.Column(db.Integer, db.ForeignKey('Artists.id'), nullable=False)
    artist = db.relationship('Artist', back_populates='shows', lazy='joined')
