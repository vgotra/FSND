from data_access.entities.Show import Show


class ShowsRepository:
    def __init__(self, db):
        self.db = db

    def get_all_shows(self):
        shows = self.db.session.query(Show) \
            .order_by(Show.start_time) \
            .all()

        result = [
            {
                "venue_id": show.venue.id,
                "venue_name": show.venue.name,
                "artist_id": show.artist.id,
                "artist_name": show.artist.name,
                "artist_image_link": show.artist.image_link,
                "start_time": show.start_time.isoformat()
            } for show in shows
        ]

        return result
