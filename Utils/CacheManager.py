import time

from Utils.Database import Database

MAX_CACHE_TIME = 60 *10 #10 minutes

class CacheManager:
    def __init__(self, db: Database = None):
        if db is None:
            db = Database()
        self.db = db

    def write_cache(self, primary_key, secondary_key, data):
        self.db.do_query("""REPLACE INTO CACHE_DATA (PRIMARY_KEY, SECONDARY_KEY, TIMESTAMP, DATA) 
        VALUES (%s, %s, %s, %s)""", (primary_key, secondary_key, int(time.time()), data))

    def read_cache(self, primary_key, secondary_key, max_time=MAX_CACHE_TIME):
        try:
            result = self.db.select_one("SELECT * FROM CACHE_DATA WHERE PRIMARY_KEY = %s AND SECONDARY_KEY = %s;",
                                    (primary_key, secondary_key,))
            id, primary_key, secondary_key, timestamp, data = result

            if (time.time() - int(timestamp)) > max_time:
                return None
            else:
                return data
        except:
            return None
