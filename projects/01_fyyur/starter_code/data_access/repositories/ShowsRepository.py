from data_access.conversion_helpers.ShowsConversion import ShowsConversion
from data_access.entities.Show import Show


class ShowsRepository:
    def __init__(self, db):
        self.db = db

    def get_all_shows(self):
        shows = self.db.session.query(Show).order_by(Show.start_time).all()

        result = [ShowsConversion.convert_to_show_model(show) for show in shows]
        return result

    def create_show(self, show):
        new_show = Show()
        new_show.artist_id = show.artist_id.data
        new_show.venue_id = show.venue_id.data
        new_show.start_time = show.start_time.data

        self.db.session.add(new_show)
        self.db.session.commit()
