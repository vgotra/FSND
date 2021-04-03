from datetime import datetime

from data_access.entities.Artist import Artist


class ArtistsConversion:

    def convert_to_artist_model(artist: Artist):
        result = {
            "id": artist.id,
            "name": artist.name,
            "genres": [genre.name for genre in artist.genres],
            "city": artist.city.name,
            "state": artist.city.state,
            "phone": artist.phone,
            "website_link": artist.website_link,
            "facebook_link": artist.facebook_link,
            "seeking_venue": artist.seeking_venue,
            "seeking_description": artist.seeking_description,
            "image_link": artist.image_link
        }
        return result

    def convert_to_artist_with_shows_model(artist: Artist):
        past_shows = [x for x in artist.shows if x.start_time <= datetime.utcnow()]
        upcoming_shows = [x for x in artist.shows if x.start_time >= datetime.utcnow()]

        result = {
            "id": artist.id,
            "name": artist.name,
            "genres": [genre.name for genre in artist.genres],
            "city": artist.city.name,
            "state": artist.city.state,
            "phone": artist.phone,
            "website_link": artist.website_link,
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
            "past_shows_count": len(past_shows),
            "upcoming_shows_count": len(upcoming_shows)
        }
        return result

    def convert_to_artist_search_results_model(count, artists: list[Artist]):
        results = {
            "count": count,
            "data": [{
                "id": artist.id,
                "name": artist.name,
                "num_upcoming_shows": sum(map(lambda x: x.start_time >= datetime.utcnow(), artist.shows)),
            } for artist in artists]
        }
        return results
