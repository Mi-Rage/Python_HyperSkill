# Write your code here
import random


def greeting():
    print("H A N G M A N")
    print()


def hide_letter(word):
    return list("-" * len(word))


def get_letter(hidden_word):
    while True:
        print_result(hidden_word)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter.\n")
        elif 97 > ord(letter) or ord(letter) > 122:
            print("Please enter a lowercase English letter.\n")
        else:
            return letter


def print_result(list_of):
    result = ""
    for index in range(len(list_of)):
        result += list_of[index]
    print(result)


def update_hidden_word(list_of, secret_word, letter):
    for index in range(len(secret_word)):
        if letter == secret_word[index]:
            list_of[index] = letter
    return list_of


def farewell(is_win):
    if is_win:
        print("You guessed the word!")
        print("You survived!\n")
    else:
        print("You lost!\n")


def game():
    greeting()

    secret_list = ('python', 'java', 'kotlin', 'javascript')
    secret_word = random.choice(secret_list)
    hidden_word = hide_letter(secret_word)

    turn = 8
    is_win = False
    used_letters = list()

    while turn > 0:
        letter = get_letter(hidden_word)

        if letter in used_letters:
            print("You've already guessed this letter")
        elif letter in secret_word:
            hidden_word = update_hidden_word(hidden_word, secret_word, letter)
        else:
            print("That letter doesn't appear in the word")
            turn -= 1

        used_letters.append(letter)

        if "-" not in hidden_word:
            print()
            print(secret_word)
            is_win = True
            break
        elif turn > 0:
            print()

    farewell(is_win)


def init_game():
    while True:
        mode = input('Type "play" to play the game, "exit" to quit: ')
        if mode == "play":
            game()
        else:
            break


init_game()
