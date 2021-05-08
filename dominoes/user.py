import random

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
        elif turn < 0:
            item = self.user_set.pop(abs(turn) - 1)
            snake.insert(0, item)
        else:
            item = self.user_set.pop(abs(turn) - 1)
            snake.append(item)

    def get_ai_turn(self, snake, stock):
        input()
        item = random.choice(self.user_set)
        self.user_set.remove(item)
        snake.append(item)

