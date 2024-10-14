import config
import sqlite3

class Database:

    #database connector
    connector = ""
    cursor = ""

    def __init__(self,app):
        self.connector = sqlite3.connect(config.DATABASE_NAME)
        self.cursor = self.connector.cursor()

    def query(self, sql):
        return self.cursor.execute(sql)
    
    def prepared_query(self, sql, params):
        return self.cursor.execute(sql, params)