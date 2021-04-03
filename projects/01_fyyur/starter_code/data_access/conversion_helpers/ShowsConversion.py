from data_access.entities.Show import Show


class ShowsConversion:

    def convert_to_show_model(show: Show):
        result = {
            "venue_id": show.venue.id,
            "venue_name": show.venue.name,
            "artist_id": show.artist.id,
            "artist_name": show.artist.name,
            "artist_image_link": show.artist.image_link,
            "start_time": show.start_time.isoformat()
        }
        return result
