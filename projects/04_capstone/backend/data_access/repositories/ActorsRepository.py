from data_access.entities.Actor import Actor
from data_access.exceptions.NotFound import NotFound


class ActorsRepository:
    def __init__(self, db):
        self.db = db
        self.per_page = 10

    def get_all(self, page=1, search_phrase=None):
        actors_query = self.db.session.query(Actor).order_by(Actor.id)
        if search_phrase:
            actors_query = actors_query.filter(Actor.name.ilike("%{}%".format(search_phrase)))
        actors = actors_query.paginate(page, self.per_page, error_out=False)
        return actors

    def get(self, id):
        actor = self.db.session.query(Actor).filter(Actor.id == id).first()
        return actor

    def update(self, id, actor):
        actor_db = self.db.session.query(Actor).filter(Actor.id == id).first()
        if not actor_db:
            raise NotFound("Entity is not found")
        self.set_data(actor_db, actor)
        self.db.session.commit()
        return actor_db

    def create(self, actor):
        new_actor = Actor()
        self.set_data(new_actor, actor)
        self.db.session.add(new_actor)
        self.db.session.commit()
        return new_actor

    def delete(self, id):
        actor_db = self.db.session.query(Actor).filter(Actor.id == id).first()
        if not actor_db:
            raise NotFound("Entity is not found")
        self.db.session.delete(actor_db)
        self.db.session.commit()
        return id

    def set_data(self, actor_db, actor_model):
        actor_db.name = actor_model["name"]
        actor_db.birthday = actor_model["birthday"]
        actor_db.profile_url = actor_model["profile_url"]
        actor_db.sex = actor_model["sex"]
        actor_db.photo_url = actor_model["photo_url"]
