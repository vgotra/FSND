from datetime import datetime


class VenuesConversion:

    def convert_to_venues_grouped_by_city(cities):
        results = [
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
        return results

    def convert_to_venue_model(venue):
        result = {
            "id": venue.id,
            "name": venue.name,
            "genres": [genre.name for genre in venue.genres],
            "address": venue.address,
            "city": venue.city.name,
            "state": venue.city.state,
            "phone": venue.phone,
            "website_link": venue.website_link,
            "facebook_link": venue.facebook_link,
            "seeking_talent": venue.seeking_talent,
            "seeking_description": venue.seeking_description,
            "image_link": venue.image_link,
        }
        return result

    def convert_to_venue_with_shows_model(venue):
        past_shows = [x for x in venue.shows if x.start_time <= datetime.utcnow()]
        upcoming_shows = [x for x in venue.shows if x.start_time >= datetime.utcnow()]

        result = {
            "id": venue.id,
            "name": venue.name,
            "genres": [genre.name for genre in venue.genres],
            "address": venue.address,
            "city": venue.city.name,
            "state": venue.city.state,
            "phone": venue.phone,
            "website_link": venue.website_link,
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
            "past_shows_count": len(past_shows),
            "upcoming_shows_count": len(upcoming_shows),
        }
        return result

    def convert_to_venue_search_results_model(count, venues):
        results = {
            "count": count,
            "data": [{
                "id": venue.id,
                "name": venue.name,
                "num_upcoming_shows": sum(map(lambda x: x.start_time >= datetime.utcnow(), venue.shows)),
            } for venue in venues]
        }
        return results
