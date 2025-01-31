import mysql.connector as connector

class Database:
    def __init__(self):
        self.data = connector.connect(host='localhost',port='3306',)