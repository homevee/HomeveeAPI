from HomeveeAPI.Utils.Database import Database


class ActivityManager:
    def __init__(self, language):
        self.language = language
        return

    def get_random(self, categories=None):
        db = Database()
        id, activity, language = db.select_one("SELECT * FROM `ACTIVITIES` ORDER BY RAND() LIMIT 1;", ())
        return {'activity': activity}

    def get_random_multiple(self, categories=None, limit=1):
        db = Database()
        results = db.select_all("SELECT * FROM `ACTIVITIES` ORDER BY RAND() LIMIT "+str(int(limit))+";", ())
        activities = []
        for result in results:
            id, activity, language = result
            activities.append(activity)
        return {'activities': activities}