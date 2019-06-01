from Utils.Database import Database


class FoodManager:
    def __init__(self):
        return

    def search_food(self, keyword):
        db = Database()
        id, language, joke = db.select_one("SELECT * FROM `JOKES` ORDER BY RAND() LIMIT 1;", ())
        return {'joke': joke}