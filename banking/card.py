import random


class Card:

    def __init__(self):
        self.iin = 400000
        self.checksum = 5
        self.digit_in_acc_number = 9
        self.pin_digit = 4
        self.card_number = self.create_card_number()
        self.pin = self.create_pin()

    def create_card_number(self):
        acc_number = ""
        for n in range(self.digit_in_acc_number):
            acc_number += str(random.randint(0, 9))
        return str(self.iin) + acc_number + str(self.checksum)

    def create_pin(self):
        new_pin = ""
        for n in range(self.pin_digit):
            new_pin += str(random.randint(0, 9))
        return new_pin
