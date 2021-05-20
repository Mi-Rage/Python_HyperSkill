class UserInterface:

    def __init__(self):
        self.menu_level = 0

    def get_option_main_menu(self):
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        option = int(input())
        self.menu_level = option
        return option

    def get_option_account_menu(self):
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")
        option = int(input())
        self.menu_level = option
        return option

    def output_new_account(self, new_card):
        print("Your card has been created")
        print("Your card number:")
        print(new_card.card_number)
        print("Your card PIN:")
        print(new_card.pin)

    def ask_card_number(self):
        print("Enter your card number:")
        return input()

    def ask_card_pin(self):
        print("Enter your PIN:")
        return input()

    def output_login_success(self):
        print("You have successfully logged in!")

    def output_login_failed(self):
        print("Wrong card number or PIN!")

    def output_log_out(self):
        print("You have successfully logged out!")

    def output_balance(self, balance):
        print(f"Balance: {balance}")

    def output_shut_down(self):
        self.menu_level = 0
        print("Bye!")
