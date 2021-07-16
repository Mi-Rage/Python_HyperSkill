import os
import sqlite3


def is_db_file_not_exist(db_file_name):
    is_file_exist = os.path.exists(db_file_name)
    if is_file_exist:
        print("File exist!")
        return False
    else:
        return True


class Storage:
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        if is_db_file_not_exist(self.db_file_name):
            self.conn = sqlite3.connect(self.db_file_name)
            self.create_table()
            self.fill_table()
            self.conn.close()

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY AUTOINCREMENT, meal_name TEXT UNIQUE NOT NULL);')
        cur.execute(
            'CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, ingredient_name TEXT NOT NULL UNIQUE);')
        cur.execute(
            'CREATE TABLE IF NOT EXISTS measures (measure_id INTEGER PRIMARY KEY AUTOINCREMENT, measure_name TEXT UNIQUE);')
        self.conn.commit()

    def fill_table(self):
        cur = self.conn.cursor()
        request = f'INSERT INTO meals (meal_name) VALUES ("breakfast"), ("brunch"), ("lunch"), ("supper");'
        cur.execute(request)
        request = f'INSERT INTO ingredients (ingredient_name) VALUES ("milk"), ("cacao"), ("strawberry"), ("blueberry"), ("blackberry"), ("sugar");'
        cur.execute(request)
        request = f'INSERT INTO measures (measure_name) VALUES ("ml"), ("g"), ("l"), ("cup"), ("tbsp"), ("tsp"), ("dsp"), ("");'
        cur.execute(request)
        self.conn.commit()

    def print_table(self):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        request = f'SELECT * FROM meals;'
        cur.execute(request)
        result = cur.fetchall()
        if result is None:
            print("There's no one here....")
        else:
            print(result)
        self.conn.close()
