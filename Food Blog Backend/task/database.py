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
            (
            meal_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            meal_name TEXT UNIQUE NOT NULL
            );''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS ingredients 
            (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ingredient_name TEXT NOT NULL UNIQUE
            );''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS measures 
            (
            measure_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            measure_name TEXT UNIQUE
            );''')
        self.conn.commit()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS recipes 
            (
            recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            recipe_name TEXT NOT NULL, 
            recipe_description TEXT
            );''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS serve
            (
            serve_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            recipe_id INTEGER NOT NULL, 
            meal_id INTEGER NOT NULL,
            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
            FOREIGN KEY(meal_id) REFERENCES meals(meal_id)
            );''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS quantity
            (
            quantity_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            measure_id INTEGER NOT NULL, 
            ingredient_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL, 
            recipe_id INTEGER NOT NULL, 
            FOREIGN KEY(measure_id) REFERENCES measures (measure_id),
            FOREIGN KEY(ingredient_id) REFERENCES ingredients (ingredient_id), 
            FOREIGN KEY(recipe_id) REFERENCES recipes (recipe_id)
            );''')
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

    def get_measure_id(self, value):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        request = f'SELECT measure_id FROM measures WHERE measure_name = "{value}";'
        cur.execute(request)
        result = cur.fetchone()
        result = result[0] if result is not None else None
        return result

    def get_id_from_table(self, table_name, value):
        ingredients = self.get_data_from_table(table_name)
        count = 0
        result = None
        for item in ingredients:
            if value in item[1]:
                count += 1
                result = item[0]
        return result if count == 1 else None

    def save_quantity(self, quantity, recipe_id, measure_id, ingredient_id):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        request = f'INSERT INTO quantity (quantity, recipe_id, measure_id, ingredient_id) VALUES ({quantity}, {recipe_id}, {measure_id}, {ingredient_id});'
        cur.execute(request)
        self.conn.commit()
        self.conn.close()

    def get_list_id_from_table_meal(self, values):
        id_list = []
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        for v in values:
            request = f'SELECT meal_id FROM meals WHERE meal_name="{v}";'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchone()
            id_list.append(result[0])
        self.conn.close()
        return id_list

    def get_list_id_from_table_ing(self, values):
        id_list = []
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        for v in values:

            request = f'SELECT ingredient_id FROM ingredients WHERE ingredient_name="{v}";'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchone()
            if result is not None:
                id_list.append(result[0])
            else:
                id_list.append(99)
        self.conn.close()
        return id_list

    def get_recipe_id_list(self, values):
        id_list = []
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        for v in values:
            request = f'SELECT recipe_id FROM quantity WHERE ingredient_id={v};'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchall()
            id_list.append(result)
            print("recipe_res ", result)
        self.conn.close()
        result_list = []
        found = None
        for item in id_list[0]:
            for i in range(len(id_list)-1):
                if item not in id_list[i+1]:
                    found = None
                    break
                else:
                    found = item[0]
            if found is not None:
                result_list.append(found)
                found = None
        print(result_list)
        return result_list

    def get_name_from_recipe(self, values):
        id_list = []
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        for v in values:
            request = f'SELECT recipe_name FROM recipes WHERE recipe_id="{v}";'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchone()
            id_list.append(result[0])
        self.conn.close()
        return id_list

    def get_recipe_in_serve(self, meals_id, ingr_id):
        self.conn = sqlite3.connect(self.db_file_name)
        cur = self.conn.cursor()
        recipe_list = []
        for v in meals_id:
            request = f'SELECT recipe_id FROM serve WHERE meal_id={v};'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchall()
            recipe_list.append([r[0] for r in result])
        rec_set = set()
        for r in recipe_list:
            for item in r:
                rec_set.add(item)
        print("reipe_is_list_from_serve",recipe_list)
        print("reipe_set",rec_set)
        ing_list = dict()
        cur = self.conn.cursor()
        for v in rec_set:
            request = f'SELECT ingredient_id FROM quantity WHERE recipe_id={v};'
            cur.execute(request)
            self.conn.commit()
            result = cur.fetchall()
            ing_list[v]=[r[0] for r in result]
        print("new_rec_list", ing_list)
        found_reciep_list = []
        found = None
        for k in ing_list.keys():
            for v in ingr_id:
                if v not in ing_list.get(k):
                    found = None
                    break
                else:
                    found = k
            if found is not None:
                found_reciep_list.append(found)
        print("id рецептов", found_reciep_list)
        return found_reciep_list
