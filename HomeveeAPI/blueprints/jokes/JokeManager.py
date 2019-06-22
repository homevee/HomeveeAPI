from HomeveeAPI.Utils.Database import Database


class JokeManager:
    def __init__(self, language):
        self.language = language
        return

    def get_random(self, categories=None):
        db = Database()
        id, joke, language = db.select_one("SELECT * FROM `JOKES` ORDER BY RAND() LIMIT 1;", ())
        return {'joke': joke}