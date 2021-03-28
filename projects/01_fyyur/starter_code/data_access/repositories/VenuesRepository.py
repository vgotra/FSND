from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import contains_eager
from data_access.entities.Show import Show
from data_access.entities.City import City
from data_access.entities.Venue import Venue


class VenuesRepository:
    def __init__(self, db):
        self.db = db

    def get_venues_grouped_by_city(self):
        cities = self.db.session.query(City) \
            .join(Venue, isouter=True) \
            .join(Show, isouter=True) \
            .options(contains_eager(City.venues).contains_eager(Venue.shows)) \
            .order_by(desc(City.name)) \
            .all()

        result = [
            {
                "city": city.name,
                "state": city.state,
                "venues": [
                    {
                        "id": venue.id,
                        "name": venue.name,
                        "num_upcoming_shows": sum(map(lambda x: x.start_time >= datetime.utcnow(), venue.shows))
                    }
                    for venue in city.venues]
            } for city in cities
        ]

        return result

    def get_venue_by_id(self, venue_id):
        venue = self.db.session.query(Venue) \
            .filter_by(id=venue_id) \
            .first()

        past_shows = filter(lambda x: x.start_time <= datetime.utcnow(), venue.shows)
        upcoming_shows = filter(lambda x: x.start_time >= datetime.utcnow(), venue.shows)

        result = {
            "id": venue.id,
            "name": venue.name,
            "genres": [genre.name for genre in venue.genres],
            "address": venue.address,
            "city": venue.city.name,
            "state": venue.city.state,
            "phone": venue.phone,
            "website": venue.website,
            "facebook_link": venue.facebook_link,
            "seeking_talent": venue.seeking_talent,
            "seeking_description": venue.seeking_description,
            "image_link": venue.image_link,
            "past_shows": [{"artist_id": show.artist.id, "artist_name": show.artist.name,
                            "artist_image_link": show.artist.image_link, "start_time": show.start_time.isoformat()}
                           for show in past_shows],
            "upcoming_shows": [{"artist_id": show.artist.id, "artist_name": show.artist.name,
                                "artist_image_link": show.artist.image_link, "start_time": show.start_time.isoformat()}
                               for show in upcoming_shows],
            "past_shows_count": sum(map(lambda x: x.start_time <= datetime.utcnow(), venue.shows)),
            "upcoming_shows_count": sum(map(lambda x: x.start_time >= datetime.utcnow(), venue.shows)),
        }

        return result
