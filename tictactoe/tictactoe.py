empty_symbol = '_'
player1 = 'X'
player2 = 'O'


def init_cells(symbol):
    result = [[symbol, symbol, symbol], [symbol, symbol, symbol], [symbol, symbol, symbol]]
    return result


def print_field(source_field):
    print("---------")
    for row in range(3):
        print("| {0} {1} {2} |".format(source_field[row][0], source_field[row][1], source_field[row][2]))
    print("---------")


def check_diag_win(symbol, source_field):
    left_right_diag = True
    right_left_diag = True

    for i in range(3):
        left_right_diag &= source_field[i][i] == symbol
        right_left_diag &= source_field[3 - i - 1][i] == symbol

    if left_right_diag or right_left_diag:
        return True
    else:
        return False


def check_col_row_win(symbol, source_field):
    for row in range(3):
        rows_win = True
        columns_win = True

        for col in range(3):
            rows_win &= source_field[row][col] == symbol
            columns_win &= source_field[col][row] == symbol

        if rows_win or rows_win:
            return True

    return False


def is_end_game(source_field):
    total_symbols = [symbol for row in source_field for symbol in row]
    total_space = total_symbols.count(empty_symbol)

    line_x_win = check_col_row_win(player1, source_field)
    line_o_win = check_col_row_win(player2, source_field)

    if check_diag_win(player1, source_field) or line_x_win:
        print(f"{player1} wins")
        return True

    if check_diag_win(player2, source_field) or line_o_win:
        print(f"{player2} wins")
        return True

    if total_space == 0:
        print("Draw")
        return True
    else:
        return False


def get_coordinates(source_field):
    while True:
        user_turn = input("Enter the coordinates: ").split()

        is_not_digit = True
        while is_not_digit:
            if not all(coord.isdigit() for coord in user_turn):
                print("You should enter numbers!")
                user_turn = input("Enter the coordinates: ").split()
                break
            else:
                is_not_digit = False

        user_coord = [int(c) for c in user_turn]

        if len(user_coord) < 2:
            print("Error! Need 2 coordinates!")
        elif not all(coord in range(1, 4) for coord in user_coord):
            print("Coordinates should be from 1 to 3!")
        elif source_field[user_coord[0]-1][user_coord[1]-1] != empty_symbol:
            print("This cell is occupied! Choose another one!")
        else:
            return user_coord


def update_field(coordinates, source_field, player_symbol):
    row = coordinates[0] - 1
    col = coordinates[1] - 1
    source_field[row][col] = player_symbol
    return source_field


def player_turn(player_symbol, field):
    player_coordinates = get_coordinates(field)
    return update_field(player_coordinates, field, player_symbol)


def main():
    player_symbol = player1
    field = init_cells(empty_symbol)
    print_field(field)
    while True:
        field = player_turn(player_symbol, field)
        print_field(field)
        if is_end_game(field):
            break
        else:
            player_symbol = player2 if player_symbol == player1 else player1


if __name__ == '__main__':
    main()
