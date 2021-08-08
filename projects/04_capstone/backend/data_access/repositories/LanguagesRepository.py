from data_access.entities.Language import Language
from data_access.exceptions.NotFound import NotFound


class LanguagesRepository:
    def __init__(self, db):
        self.db = db
        self.per_page = 10

    def get_all(self, page=1, search_phrase=None):
        languages_query = self.db.session.query(Language).order_by(Language.id)
        if search_phrase:
            languages_query = languages_query.filter(Language.name.ilike("%{}%".format(search_phrase)))
        languages = languages_query.paginate(page, self.per_page, error_out=False)
        return languages

    def get(self, id):
        language = self.db.session.query(Language).filter(Language.id == id).first()
        return language

    def update(self, id, language):
        language_db = self.db.session.query(Language).filter(Language.id == id).first()
        if not language_db:
            raise NotFound("Entity is not found")
        self.set_data(language_db, language)
        self.db.session.commit()
        return language_db

    def create(self, language):
        new_language = Language()
        self.set_data(new_language, language)
        self.db.session.add(new_language)
        self.db.session.commit()

    def set_data(language_db, language_model):
        language_db.name = language_model.name
        language_db.phone = language_model.birthday
        language_db.sex = language_model.sex
        language_db.profile_url = language_model.profile_url
        language_db.photo_url = language_model.photo_url
