from data_access.entities.Actor import Actor


class ActorsRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, search_phrase):
        actors_query = self.db.session.query(Actor).order_by(Actor.id)
        if search_phrase:
            actors_query = actors_query.filter(Actor.name.ilike("%{}%".format(search_phrase)))
        count = actors_query.count()
        actors = actors_query.all()
        return (count, actors)

    def get(self, id):
        actor = self.db.session.query(Actor).filter(Actor.id == id).first()
        return actor

    def update(self, id, actor):
        actor_db = self.db.session.query(Actor).filter(Actor.id == id).first()
        self.set_data(actor_db, actor)
        self.db.session.commit()

    def create(self, actor):
        new_actor = Actor()
        self.set_data(new_actor, actor)
        self.db.session.add(new_actor)
        self.db.session.commit()

    def set_data(actor_db, actor_model):
        actor_db.name = actor_model.name
        actor_db.phone = actor_model.birthday
        actor_db.sex = actor_model.sex
        actor_db.profile_url = actor_model.profile_url
        actor_db.photo_url = actor_model.photo_url
