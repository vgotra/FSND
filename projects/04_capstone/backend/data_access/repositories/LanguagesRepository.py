from data_access.entities.Language import Language


class LanguagesRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self, search_phrase):
        languages_query = self.db.session.query(Language).order_by(Language.id)
        if search_phrase:
            languages_query = languages_query.filter(Language.name.ilike("%{}%".format(search_phrase)))
        count = languages_query.count()
        languages = languages_query.all()
        return (count, languages)

    def get(self, id):
        language = self.db.session.query(Language).filter(Language.id == id).first()
        return language

    def update(self, id, language):
        language_db = self.db.session.query(Language).filter(Language.id == id).first()
        self.set_data(language_db, language)
        self.db.session.commit()

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
