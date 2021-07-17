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
        cur.execute('PRAGMA foreign_keys = ON;')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS meals 
            (meal_id INTEGER PRIMARY KEY AUTOINCREMENT, meal_name TEXT UNIQUE NOT NULL);''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS ingredients 
            (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, ingredient_name TEXT NOT NULL UNIQUE);''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS measures 
            (measure_id INTEGER PRIMARY KEY AUTOINCREMENT, measure_name TEXT UNIQUE);''')
        self.conn.commit()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS recipes 
            (recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, recipe_name TEXT NOT NULL, recipe_description TEXT);''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS serve
            (serve_id INTEGER PRIMARY KEY AUTOINCREMENT, recipe_id INTEGER NOT NULL, meal_id INTEGER NOT NULL,
            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
            FOREIGN KEY(meal_id) REFERENCES meals(meal_id));''')
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

    def save_recipe(self, recipe_name, recipe_desc):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        request = f'INSERT INTO recipes (recipe_name, recipe_description) VALUES ("{recipe_name}", "{recipe_desc}");'
        last_id = cur.execute(request).lastrowid
        self.conn.commit()
        self.conn.close()
        return last_id

    def print_table(self, table_name):
        result = self.get_data_from_table(table_name)
        if result is None:
            print("There's no one here....")
        else:
            print(result)
        self.conn.close()

    def get_data_from_table(self, table_name):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        request = f'SELECT * FROM {table_name};'
        cur.execute(request)
        result = cur.fetchall()
        self.conn.close()
        return result

    def save_serve(self, selected_periods, recipe_id):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        for item in selected_periods:
            request = f'INSERT INTO serve (meal_id, recipe_id) VALUES ({int(item)}, {int(recipe_id)});'
            cur.execute(request)
        self.conn.commit()
        self.conn.close()
