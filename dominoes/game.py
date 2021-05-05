class Game:
    snake = []
    next_turn = None

    def __init__(self, stock, users):
        self.stock = stock
        self.users = users

    def get_first_move(self):
        doubles = []
        for each_user in self.users:
            doubles.append(each_user.get_max_double())

        index_dbl = 0
        max_double = 0
        for dbl in doubles:
            if len(dbl) > 0:
                sum_double = dbl[0] * 2
                if sum_double > max_double:
                    max_double = sum_double
                    index_dbl = doubles.index(dbl)
        self.users[index_dbl].user_set.remove(doubles[index_dbl])
        self.snake.append(doubles[index_dbl])
        self.next_turn = self.users[(index_dbl + 1) % len(self.users)]

    def print_snake(self):
        for piece in self.snake:
            print(piece)

    def print_status(self):
        if self.next_turn.user_name == "Player":
            print("Status: It's your turn to make a move. Enter your command.")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")

    def print_situation(self):
        print("=" * 70)
        print(f"Stock size: {len(self.stock.pieces)}")
        print(f"Computer pieces: {len(self.users[0].user_set)}\n")
        self.print_snake()
        print()
        print("Your pieces:")
        for index in range(len(self.users[1].user_set)):
            print(f"{index + 1}: {self.users[1].user_set[index]}")
        self.print_status()
