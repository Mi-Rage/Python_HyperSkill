import random


class Card:

    def __init__(self):
        self.iin = 400000
        self.digit_in_acc_number = 9
        self.pin_digit = 4
        self.check_sum = 0
        self.card_number = self.create_card_number()
        self.pin = self.create_pin()

    def create_card_number(self):
        acc_number = ""
        for n in range(self.digit_in_acc_number):
            acc_number += str(random.randint(0, 9))
        number_without_checksum = str(self.iin) + acc_number
        check_sum = self.get_checksum(number_without_checksum)
        return str(self.iin) + acc_number + str(check_sum)

    def create_pin(self):
        new_pin = ""
        for n in range(self.pin_digit):
            new_pin += str(random.randint(0, 9))
        return new_pin

    def get_checksum(self, checked_card_number):
        result = 0
        for index in range(15):
            item = int(checked_card_number[index])
            if index % 2 == 0:
                item = item * 2
                if item > 9:
                    item = item - 9
            print(item)
            result += item
        if result % 10 != 0:
            self.check_sum = 10 - result % 10
        else:
            self.check_sum = 0
        return self.check_sum
