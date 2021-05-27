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

    def is_card_exist(self, card_number):
        cur = self.conn.cursor()
        request = f'SELECT id FROM card WHERE number = {card_number};'
        cur.execute(request)
        result = cur.fetchone()
        if result is None:
            return result
        else:
            return result[0]

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

    def add_income_to_account(self, income):
        cur = self.conn.cursor()
        request = f'UPDATE card SET balance = {income} WHERE id = {self.current_acc_id};'
        cur.execute(request)
        self.conn.commit()

    def is_enough_money(self, money_to_transfer):
        if money_to_transfer < self.request_balance():
            return True
        else:
            return False

    def do_transfer(self, destination_id, money_to_transfer):
        tmp_id = self.current_acc_id
        sponsor_balance = self.request_balance() - money_to_transfer
        self.add_income_to_account(sponsor_balance)
        self.current_acc_id = destination_id
        destination_balance = self.request_balance() + money_to_transfer
        self.add_income_to_account(destination_balance)
        self.current_acc_id = tmp_id

    def delete_account(self):
        cur = self.conn.cursor()
        request = f'DELETE FROM card WHERE id = {self.current_acc_id};'
        cur.execute(request)
        self.conn.commit()
        self.log_out()

    def log_out(self):
        self.current_acc_id = -1
