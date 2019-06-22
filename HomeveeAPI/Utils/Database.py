import mysql.connector

from HomeveeAPI.Utils import Utils


class Database():
    def __init__(self, db=None):
        if db is None:
            db = self.get_database_con()
        self.db = db

    def do_query(self, sql: str, params: tuple):
        """
        Executes the given sql-statement and returns a pointer to the resulting cursor
        :param sql: the sql-statement as a string
        :param params: the parameters-dict
        :return: the cursor after executing the query
        """
        mycursor = self.db.cursor()
        print(sql, params)
        mycursor.execute(sql, params)
        return mycursor

    def select_one(self, sql: str, params: tuple):
        """
        Selects a single result from the given query
        :param sql: the sql query
        :param params: the params
        :return: the first found item
        """
        cursor = self.do_query(sql, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def select_all(self, sql: str, params: tuple):
        """
        Selects all results from the given query
        :param sql: the sql query
        :param params: the sql params
        :return: all found items
        """
        cursor = self.do_query(sql, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    def get_database_con(self):
        """
        Returns a connection to the database
        :return: the database connection
        """
        data = Utils.get_config_data()
        host = data['db_host']
        user = data['db_user']
        passwd = data['db_password']
        database = data['db_name']
        db = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        return db