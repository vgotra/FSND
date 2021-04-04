from sqlalchemy import desc

from data_access.conversion_helpers.VenuesConversion import VenuesConversion
from data_access.entities.City import City
from data_access.entities.Genre import Genre
from data_access.entities.Show import Show
from data_access.entities.Venue import Venue


class VenuesRepository:
    def __init__(self, db):
        self.db = db

    def get_venues_grouped_by_city(self):
        cities = self.db.session.query(City) \
            .join(City.venues, isouter=True) \
            .join(Venue.shows, isouter=True) \
            .order_by(desc(City.name)) \
            .all()

        result = VenuesConversion.convert_to_venues_grouped_by_city(cities)
        return result

    def get_venue_by_id(self, venue_id):
        venue = self.db.session.query(Venue) \
            .join(Venue.city) \
            .join(Venue.genres) \
            .filter(Venue.id == venue_id).first()

        result = VenuesConversion.convert_to_venue_model(venue)
        return result

    def get_venue_with_shows_by_id(self, venue_id):
        venue = self.db.session.query(Venue) \
            .join(Venue.city) \
            .join(Venue.shows) \
            .join(Venue.genres) \
            .filter(Venue.id == venue_id).first()

        result = VenuesConversion.convert_to_venue_with_shows_model(venue)
        return result

    def search_venues(self, search_term):
        venues_query = self.db.session.query(Venue) \
            .join(Venue.city) \
            .join(Venue.shows) \
            .filter(Venue.name.ilike("%{}%".format(search_term)))

        count = venues_query.count()
        venues = venues_query.all()

        result = VenuesConversion.convert_to_venue_search_results_model(count, venues)
        return result

    def save_venue(self, venue_id, venue):
        venue_db = self.db.session.query(Venue).join(City).filter(Venue.id == venue_id).first()

        venue_db.name = venue.name.data
        venue_db.phone = venue.phone.data
        venue_db.address = venue.address.data
        venue_db.website_link = venue.website_link.data
        venue_db.facebook_link = venue.facebook_link.data
        venue_db.seeking_talent = venue.seeking_talent.data
        venue_db.seeking_description = venue.seeking_description.data
        venue_db.image_link = venue.image_link.data

        with self.db.session.no_autoflush:
            if set([genre.name for genre in venue_db.genres]).symmetric_difference(set(venue.genres.data)):
                all_genres = self.db.session.query(Genre).all()
                venue_db_genres_names = [genre.name for genre in venue_db.genres]
                # delete
                venue_db.genres = [genre for genre in venue_db.genres if genre.name in venue.genres.data]
                # create
                genres_to_create = [genre for genre in venue.genres.data if genre not in venue_db_genres_names]
                for genre in genres_to_create:
                    genre_to_attach = next(x for x in all_genres if x.name == genre)
                    venue_db.genres.append(genre_to_attach)

            if venue_db.city.name != venue.city.data or venue_db.city.state != venue.state.data:
                city = self.db.session.query(City) \
                    .filter(City.name.ilike("%{}%".format(venue.city.data)),
                            City.state.ilike("%{}%".format(venue.state.data)), ) \
                    .first()

                if city is None:
                    city = City()
                    city.name = venue.city.data
                    city.state = venue.state.data

                venue_db.city = city

        self.db.session.commit()

    def create_venue(self, venue):
        new_venue = Venue()
        new_venue.name = venue.name.data
        new_venue.phone = venue.phone.data
        new_venue.address = venue.address.data
        new_venue.website_link = venue.website_link.data
        new_venue.facebook_link = venue.facebook_link.data
        new_venue.seeking_talent = venue.seeking_talent.data
        new_venue.seeking_description = venue.seeking_description.data
        new_venue.image_link = venue.image_link.data

        with self.db.session.no_autoflush:
            all_genres = self.db.session.query(Genre).all()
            for genre in venue.genres.data:
                genre_to_attach = next(x for x in all_genres if x.name == genre)
                new_venue.genres.append(genre_to_attach)

            city = self.db.session.query(City) \
                .filter(City.name.ilike("%{}%".format(venue.city.data)),
                        City.state.ilike("%{}%".format(venue.state.data)), ) \
                .first()

            if city is None:
                city = City()
                city.name = venue.city.data
                city.state = venue.state.data

            new_venue.city = city

        self.db.session.add(new_venue)
        self.db.session.commit()

    def delete_venue(self, venue_id):
        self.db.session.begin()
        try:
            self.db.session.query(Show).filter(Show.venue_id == venue_id).delete()
            venue = self.db.session.query(Venue).filter(Venue.id == venue_id).first()
            venue.genres = []
            self.db.session.delete(venue)

            self.db.session.commit()
        except:
            self.db.session.rollback()
            raise
