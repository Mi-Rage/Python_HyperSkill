class Storage:
    def __init__(self):
        self.account_storage = dict()

    def is_card_exist(self):
        ...

    def add_card_to_storage(self, new_card):
        self.account_storage[new_card] = 0

    def is_login(self, custom_card_number, custom_card_pin):
        result = False
        all_cards = self.account_storage.keys()
        for each_card in all_cards:
            if each_card.card_number == custom_card_number and each_card.pin == custom_card_pin:
                result = True
                break
        return result

    def request_balance(self, custom_card_number):
        result = 0
        all_cards = self.account_storage.keys()
        for each_card in all_cards:
            if each_card.card_number == custom_card_number:
                result = self.account_storage[each_card]
                break
        return result
