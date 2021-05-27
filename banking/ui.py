class UserInterface:

    def get_option_main_menu(self):
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        option = int(input())
        return option

    def get_option_account_menu(self):
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        option = int(input())
        return option

    def output_new_account(self, new_card):
        print("Your card has been created")
        print("Your card number:")
        print(new_card.card_number)
        print("Your card PIN:")
        print(new_card.pin)

    def output_succes_transfer(self):
        print("Success!")

    def output_not_enough_money(self):
        print("Not enough money!")

    def output_delete_account(self):
        print("The account has been closed!")

    def ask_card_number(self):
        print("Enter your card number:")
        return input()

    def ask_card_pin(self):
        print("Enter your PIN:")
        return input()

    def ask_income(self):
        print("Enter income:")
        return int(input())

    def ask_dest_card_number(self):
        print("Transfer")
        print("Enter card number:")
        return input()

    def ask_money_to_transfer(self):
        print("Enter how much money you want to transfer:")
        return int(input())

    def output_income_complete(self):
        print("Income was added!")

    def output_login_success(self):
        print("You have successfully logged in!")

    def output_login_failed(self):
        print("Wrong card number or PIN!")

    def output_log_out(self):
        print("You have successfully logged out!")

    def output_balance(self, balance):
        print(f"Balance: {balance}")

    def output_number_mistake(self):
        print("Probably you made a mistake in the card number. Please try again!")

    def output_card_not_exist(self):
        print("Such a card does not exist")

    def output_shut_down(self):
        self.menu_level = 0
        print("Bye!")
