from HomeveeAPI.Utils.Database import Database


class FactManager:
    def __init__(self, language):
        self.language = language
        return

    def get_random(self, categories=None):
        db = Database()
        id, fact, language = db.select_one("SELECT * FROM `USELESS_FACTS` ORDER BY RAND() LIMIT 1;", ())
        return {'fact': fact}