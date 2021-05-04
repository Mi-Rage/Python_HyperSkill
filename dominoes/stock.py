import random


class Stock:
    pieces = [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2],
              [0, 1], [3, 3], [0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5], [1, 3], [1, 4], [4, 5],
              [1, 6], [1, 1], [0, 4], [5, 5]]

    def get_item(self):
        item = random.choice(self.pieces)
        self.pieces.remove(item)
        return item
