from datetime import datetime
from data_access.entities.Artist import Artist


# TODO Why we have ROLLBACK?
# TODO Move all conversion from entity to DTO to helper methods

class ArtistsRepository:
    def __init__(self, db):
        self.db = db

    def get_all_artists(self):
        artists = self.db.session.query(Artist) \
            .order_by(Artist.name) \
            .all()

        result = [{"id": artist.id, "name": artist.name} for artist in artists]
        return result

    def get_artist_by_id(self, artist_id):
        artist = self.db.session.query(Artist) \
            .filter_by(id=artist_id) \
            .first()

        past_shows = filter(lambda x: x.start_time <= datetime.utcnow(), artist.shows)
        upcoming_shows = filter(lambda x: x.start_time >= datetime.utcnow(), artist.shows)

        result = {
            "id": artist.id,
            "name": artist.name,
            "genres": [genre.name for genre in artist.genres],
            "city": artist.city.name,
            "state": artist.city.state,
            "phone": artist.phone,
            "website": artist.website,
            "facebook_link": artist.facebook_link,
            "seeking_venue": artist.seeking_venue,
            "seeking_description": artist.seeking_description,
            "image_link": artist.image_link,
            "past_shows": [
                {"venue_id": show.venue.id, "venue_name": show.venue.name, "venue_image_link": show.venue.image_link,
                 "start_time": show.start_time.isoformat()} for show in past_shows],
            "upcoming_shows": [
                {"venue_id": show.venue.id, "venue_name": show.venue.name, "venue_image_link": show.venue.image_link,
                 "start_time": show.start_time.isoformat()} for show in upcoming_shows],
            "past_shows_count": sum(map(lambda x: x.start_time <= datetime.utcnow(), artist.shows)),
            "upcoming_shows_count": sum(map(lambda x: x.start_time >= datetime.utcnow(), artist.shows)),
        }
        return result
