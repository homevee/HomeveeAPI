import time

#from lib.Database import Database


class CacheManager():
    def __init__(self):
        self.max_cache_age = 5 * 60
        return

    def get_cached_data(self, type):
        #item = Database().select_one("SELECT * FROM TV_PROGRAMME WHERE TYPE = :type", {'type': type})

        #if item is None or (time.time() - item['TIMESTAMP']) > self.max_cache_age:
        #    return None
        #return item['DATA']
        return None

    def set_cache_data(self, type, data):
        #Database().insert("INSERT INTO TV_PROGRAMME (TIMESTAMP, TYPE, DATA) VALUES (:time, :type, :data)",
        #                {'time': int(time.time()), 'type': type, 'data': data})
        pass