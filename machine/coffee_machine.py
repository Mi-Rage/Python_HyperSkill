components = {
    'espresso': {'water': 250, 'milk': 0, 'beans': 16, 'costs': 4},
    'latte': {'water': 350, 'milk': 75, 'beans': 20, 'costs': 7},
    'cappuccino': {'water': 200, 'milk': 100, 'beans': 12, 'costs': 6}}

remains = {'money': 550, 'water': 400, 'milk': 540, 'beans': 120, 'cups': 9}


def show_remains():
    print("The coffee machine has:")
    print(f"{remains['water']} of water")
    print(f"{remains['milk']} of milk")
    print(f"{remains['beans']} of coffee beans")
    print(f"{remains['cups']} of disposable cups")
    print(f"{remains['money']} of of money")


def make_action():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            make_buy()
        elif action == 'fill':
            make_fill()
        elif action == 'take':
            make_take()
        elif action == 'remaining':
            show_remains()
        elif action == 'exit':
            break


def make_buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    mode = input()
    if mode == '1':
        make_coffee('espresso')
    elif mode == '2':
        make_coffee('latte')
    elif mode == '3':
        make_coffee('cappuccino')
    else:
        return


def make_coffee(type_coffee):
    if remains['water'] < components[type_coffee]['water']:
        print("Sorry, not enough water!")
    elif remains['milk'] < components[type_coffee]['milk']:
        print("Sorry, not enough milk!")
    elif remains['beans'] < components[type_coffee]['beans']:
        print("Sorry, not enough coffee beans!")
    else:
        print("I have enough resources, making you a coffee!")
        remains['money'] += components[type_coffee]['costs']
        remains['water'] -= components[type_coffee]['water']
        remains['milk'] -= components[type_coffee]['milk']
        remains['beans'] -= components[type_coffee]['beans']
        remains['cups'] -= 1


def make_fill():
    print("Write how many ml of water do you want to add:")
    remains['water'] += int(input())
    print("Write how many ml of milk do you want to add:")
    remains['milk'] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    remains['beans'] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    remains['cups'] += int(input())


def make_take():
    print(f"I gave you ${remains['money']}")
    remains['money'] = 0


if __name__ == '__main__':
    make_action()
