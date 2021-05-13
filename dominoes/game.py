class Game:
    snake = []

    def __init__(self, stock, ai_user, human_user):
        self.stock = stock
        self.ai_user = ai_user
        self.human_user = human_user
        self.next_turn = None
        self.status = "Continue"

    def get_first_move(self):
        max_double = max(self.ai_user.get_max_double(), self.human_user.get_max_double())
        self.snake.append(max_double)
        if max_double in self.ai_user.user_set:
            self.ai_user.user_set.remove(max_double)
            self.next_turn = self.human_user
        else:
            self.human_user.user_set.remove(max_double)
            self.next_turn = self.ai_user
        return self.next_turn

    def print_snake(self):
        result_snake = ""
        if len(self.snake) > 6:
            for i in range(len(self.snake)):
                if i <= 2:
                    result_snake += str(self.snake[i])
                elif i == 3:
                    result_snake += '...'
                elif i >= len(self.snake) - 3:
                    result_snake += str(self.snake[i])
        else:
            for i in range(len(self.snake)):
                result_snake += str(self.snake[i])

        print(result_snake)

    def print_status(self):
        if self.status == 'Continue':
            if self.next_turn.user_name == "Player":
                print("Status: It's your turn to make a move. Enter your command.")
            else:
                print("Status: Computer is about to make a move. Press Enter to continue...")
        elif self.status == 'Player win':
            print("Status: The game is over. You won!")
        elif self.status == 'Computer win':
            print("Status: The game is over. The computer won!")
        else:
            print("Status: The game is over. It's a draw!")

    def print_situation(self):
        print("=" * 70)
        print(f"Stock size: 14")
        # print(f"Stock size: {len(self.stock.pieces)}")
        print(f"Computer pieces: {len(self.ai_user.user_set)}\n")
        self.print_snake()
        print()
        print("Your pieces:")
        for index in range(len(self.human_user.user_set)):
            print(f"{index + 1}: {self.human_user.user_set[index]}")
        self.print_status()

    def make_turn(self, next_player):
        if next_player.user_name == 'Player':
            next_player.get_human_turn(self.snake, self.stock)
        else:
            next_player.get_ai_turn(self.snake, self.stock)
        self.check_status()
        return self.status

    def change_player(self, next_player):
        if next_player.user_name == 'Player':
            self.next_turn = self.ai_user
            return self.next_turn
        else:
            self.next_turn = self.human_user
            return self.next_turn

    def check_status(self):
        if self.snake[0][0] == self.snake[-1][-1]:
            identical = 0
            for item in self.snake:
                for piece in item:
                    if piece == self.snake[0][0]:
                        identical += 1
            if identical == 8:
                self.status = "Draw"
                return self.status
        if len(self.next_turn.user_set) == 0:
            if self.next_turn.user_name == 'Player':
                self.status = "Player win"
                return self.status
            else:
                self.status = "Computer win"
                return self.status
