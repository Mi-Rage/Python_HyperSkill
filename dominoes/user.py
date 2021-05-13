class User:

    def __init__(self, user_name, stock):
        self.user_set = []
        self.user_name = user_name
        for _ in range(7):
            self.user_set.append(stock.get_item())

    def get_max_double(self):
        max_double = []
        sum_item = 0
        for item in self.user_set:
            if item[0] == item[1]:
                if item[0] + item[1] > sum_item:
                    sum_item = item[0] + item[1]
                    max_double = item
        return max_double

    def get_human_turn(self, snake, stock):
        while True:
            while True:
                try:
                    turn = int(input())
                except ValueError:
                    print("Invalid input. Please try again.")
                else:
                    if abs(turn) > len(self.user_set):
                        print("Invalid input. Please try again.")
                    else:
                        break
            if turn == 0:
                self.user_set.append(stock.get_item())
                break
            else:
                if not self.is_matches(snake, turn):
                    print("Illegal move. Please try again.")
                else:
                    break

    def get_ai_turn(self, snake, stock):
        input()
        for i in range(-len(self.user_set), 0):
            if self.is_matches(snake, i):
                return

        for i in range(1, len(self.user_set) + 1):
            if self.is_matches(snake, i):
                return
        self.user_set.append(stock.get_item())

    def is_matches(self, snake, turn):
        head_snake = snake[0][0]
        tail_snake = snake[-1][-1]
        item = self.user_set[abs(turn) - 1]
        if turn < 0:
            if item[-1] == head_snake:
                self.user_set.remove(item)
                snake.insert(0, item)
                return True
            elif item[0] == head_snake:
                self.user_set.remove(item)
                snake.insert(0, list(reversed(item)))
                return True
            else:
                return False
        elif turn > 0:
            if item[0] == tail_snake:
                self.user_set.remove(item)
                snake.append(item)
                return True
            elif item[-1] == tail_snake:
                self.user_set.remove(item)
                snake.append(list(reversed(item)))
                return True
            else:
                return False
