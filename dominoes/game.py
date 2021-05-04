class Game:
    snake = []

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
        return self.users[(index_dbl + 1) % len(self.users)]
