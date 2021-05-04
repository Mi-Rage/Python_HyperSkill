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
