class Game:
    snake = []
    next_turn = None

    def __init__(self, stock, users):
        self.stock = stock
        self.users = users

    def get_first_move(self):
        max_double = max(self.users[0].get_max_double(), self.users[1].get_max_double())
        self.snake.append(max_double)
        if max_double in self.users[0].user_set:
            self.users[0].user_set.remove(max_double)
            self.next_turn = self.users[1]
        else:
            self.users[1].user_set.remove(max_double)
            self.next_turn = self.users[0]

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
