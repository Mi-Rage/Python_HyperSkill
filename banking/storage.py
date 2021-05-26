import sqlite3


class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.create_table()
        self.current_acc_id = -1

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
        self.conn.commit()

    def is_card_exist(self):
        ...

    def add_card_to_storage(self, new_card):
        cur = self.conn.cursor()
        request = f'INSERT INTO card (number, pin) VALUES ({new_card.card_number}, {new_card.pin});'
        cur.execute(request)
        self.conn.commit()

    def is_login(self, custom_card_number, custom_card_pin):
        cur = self.conn.cursor()
        request = f'SELECT id FROM card WHERE number = {custom_card_number} AND pin = {custom_card_pin};'
        cur.execute(request)
        result = cur.fetchone()
        if result is None:
            return False
        else:
            self.current_acc_id = result[0]
            return True

    def request_balance(self):
        cur = self.conn.cursor()
        request = f'SELECT balance FROM card WHERE id = {self.current_acc_id};'
        cur.execute(request)
        result = cur.fetchone()
        if result is None:
            return -1
        else:
            return result[0]

    def log_out(self):
        self.current_acc_id = -1
