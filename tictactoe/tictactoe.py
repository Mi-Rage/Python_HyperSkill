def init_cells(source_line):
    if len(source_line) < 9:
        print("Error! Length < 9!")
    else:
        result = [[j for j in source_line[index * 3:index * 3 + 3]] for index in range(3)]
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
        rows = True
        columns = True

        for col in range(3):
            rows &= source_field[row][col] == symbol
            columns &= source_field[col][row] == symbol

        if rows or columns:
            return True

    return False


def checking_status(source_field):
    total_symbols = [symbol for row in source_field for symbol in row]

    total_x = total_symbols.count('X')
    total_o = total_symbols.count('O')
    total_space = total_symbols.count('_')

    if abs(total_x - total_o) > 1:
        return "Impossible"

    line_x_win = check_col_row_win('X', source_field)
    line_o_win = check_col_row_win('O', source_field)

    if line_o_win and line_x_win:
        return "Impossible"

    if check_diag_win('X', source_field) or line_x_win:
        return "X wins"

    if check_diag_win('O', source_field) or line_o_win:
        return "O wins"

    if total_space > 0:
        return "Game not finished"
    else:
        return "Draw"


def get_coordinates(source_field):
    while True:
        user_turn = input("Enter the coordinates: ").split()

        is_not_digit = True
        while is_not_digit:
            for i in user_turn:
                if not i.isdigit():
                    is_not_digit = True
                    print("You should enter numbers!")
                    user_turn = input("Enter the coordinates: ").split()
                    break
                else:
                    is_not_digit = False

        user_coord = [int(c) for c in user_turn]

        if len(user_coord) < 2:
            print("Error! Need 2 coordinates!")
        elif user_coord[0] not in range(1, 4) or user_coord[1] not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
        elif source_field[user_coord[0]-1][user_coord[1]-1] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            return user_coord


def update_field(coordinates, source_field):
    row = coordinates[0] - 1
    col = coordinates[1] - 1
    source_field[row][col] = 'X'
    return source_field


def main():
    source = input("Enter cells: ")
    field = init_cells(source)
    print_field(field)
    coordinates = get_coordinates(field)
    field = update_field(coordinates, field)
    print_field(field)


if __name__ == '__main__':
    main()
