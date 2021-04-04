from data_access.conversion_helpers.ArtistsConversion import ArtistsConversion
from data_access.entities.Artist import Artist
from data_access.entities.City import City
from data_access.entities.Genre import Genre
from data_access.entities.Show import Show


class ArtistsRepository:
    def __init__(self, db):
        self.db = db

    def get_all_artists(self):
        artists = self.db.session.query(Artist).order_by(Artist.name).all()

        result = [{"id": artist.id, "name": artist.name} for artist in artists]
        return result

    def get_artist_by_id(self, artist_id):
        artist = self.db.session.query(Artist)\
            .join(Artist.city) \
            .join(Artist.genres) \
            .filter(Artist.id == artist_id).first()

        result = ArtistsConversion.convert_to_artist_model(artist)
        return result

    def get_artist_with_shows_by_id(self, artist_id):
        artist = self.db.session.query(Artist) \
            .join(Artist.city) \
            .join(Artist.shows) \
            .join(Artist.genres) \
            .filter(Artist.id == artist_id).first()

        result = ArtistsConversion.convert_to_artist_with_shows_model(artist)
        return result

    def search_artists(self, search_term):
        artists_query = self.db.session.query(Artist)\
            .join(Artist.city) \
            .join(Artist.shows) \
            .filter(Artist.name.ilike("%{}%".format(search_term)))

        count = artists_query.count()
        artists = artists_query.all()

        result = ArtistsConversion.convert_to_artist_search_results_model(count, artists)
        return result

    def save_artist(self, artist_id, artist):
        artist_db = self.db.session.query(Artist)\
            .join(Artist.city) \
            .join(Artist.shows) \
            .join(Artist.genres) \
            .filter(Artist.id == artist_id).first()

        artist_db.name = artist.name.data
        artist_db.phone = artist.phone.data
        artist_db.website_link = artist.website_link.data
        artist_db.facebook_link = artist.facebook_link.data
        artist_db.seeking_venue = artist.seeking_venue.data
        artist_db.seeking_description = artist.seeking_description.data
        artist_db.image_link = artist.image_link.data

        with self.db.session.no_autoflush:
            if set([genre.name for genre in artist_db.genres]).symmetric_difference(set(artist.genres.data)):
                all_genres = self.db.session.query(Genre).all()
                artist_db_genres_names = [genre.name for genre in artist_db.genres]
                # delete
                artist_db.genres = [genre for genre in artist_db.genres if genre.name in artist.genres.data]
                # create
                genres_to_create = [genre for genre in artist.genres.data if genre not in artist_db_genres_names]
                for genre in genres_to_create:
                    genre_to_attach = next(x for x in all_genres if x.name == genre)
                    artist_db.genres.append(genre_to_attach)

            if artist_db.city.name != artist.city.data or artist_db.city.state != artist.state.data:
                city = self.db.session.query(City) \
                    .filter(City.name.ilike("%{}%".format(artist.city.data)),
                            City.state.ilike("%{}%".format(artist.state.data)), ) \
                    .first()

                if city is None:
                    city = City()
                    city.name = artist.city.data
                    city.state = artist.state.data

                artist_db.city = city

        self.db.session.commit()

    def create_artist(self, artist):
        new_artist = Artist()
        new_artist.name = artist.name.data
        new_artist.phone = artist.phone.data
        new_artist.website_link = artist.website_link.data
        new_artist.facebook_link = artist.facebook_link.data
        new_artist.seeking_venue = artist.seeking_venue.data
        new_artist.seeking_description = artist.seeking_description.data
        new_artist.image_link = artist.image_link.data

        with self.db.session.no_autoflush:
            all_genres = self.db.session.query(Genre).all()
            for genre in artist.genres.data:
                genre_to_attach = next(x for x in all_genres if x.name == genre)
                new_artist.genres.append(genre_to_attach)

            city = self.db.session.query(City) \
                    .filter(City.name.ilike("%{}%".format(artist.city.data)),
                            City.state.ilike("%{}%".format(artist.state.data)), ) \
                    .first()

            if city is None:
                city = City()
                city.name = artist.city.data
                city.state = artist.state.data

            new_artist.city = city

        self.db.session.add(new_artist)
        self.db.session.commit()