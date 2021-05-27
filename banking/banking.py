import sys
import card
import ui
import storage

ui = ui.UserInterface()
storage = storage.Storage()


def create_account():
    new_card = card.Card()
    storage.add_card_to_storage(new_card)
    ui.output_new_account(new_card)


def get_balance():
    balance = storage.request_balance()
    ui.output_balance(balance)


def add_income():
    income = ui.ask_income()
    balance = storage.request_balance()
    storage.add_income_to_account(balance + income)
    ui.output_income_complete()


def do_transfer():
    dest_card_number = ui.ask_dest_card_number()
    if card.is_correct(dest_card_number):
        destination_id = storage.is_card_exist(dest_card_number)
        if destination_id is not None:
            money_to_transfer = ui.ask_money_to_transfer()
            if storage.is_enough_money(money_to_transfer):
                storage.do_transfer(destination_id, money_to_transfer)
                ui.output_succes_transfer()
            else:
                ui.output_not_enough_money()
        else:
            ui.output_card_not_exist()
    else:
        ui.output_number_mistake()


def close_account():
    storage.delete_account()
    ui.output_delete_account()


def log_out():
    storage.log_out()
    ui.output_log_out()


def log_in_account():
    custom_card_number = ui.ask_card_number()
    custom_card_pin = ui.ask_card_pin()
    if storage.is_login(custom_card_number, custom_card_pin):
        ui.output_login_success()
        while True:
            submenu_option = ui.get_option_account_menu()
            if submenu_option == 1:
                get_balance()
            elif submenu_option == 2:
                add_income()
            elif submenu_option == 3:
                do_transfer()
            elif submenu_option == 4:
                close_account()
                break
            elif submenu_option == 5:
                log_out()
                break
            elif submenu_option == 0:
                shut_down()
                break

    else:
        ui.output_login_failed()


def shut_down():
    ui.output_shut_down()
    sys.exit(0)


def bank_system():
    while True:
        menu_option = ui.get_option_main_menu()
        if menu_option == 1:
            create_account()
        elif menu_option == 2:
            log_in_account()
        elif menu_option == 0:
            shut_down()
            break


if __name__ == "__main__":
    bank_system()
