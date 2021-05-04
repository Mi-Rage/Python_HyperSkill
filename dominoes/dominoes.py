import stock
import user
import game


stock = stock.Stock()
users = [user.User('Computer', stock), user.User('Player', stock)]
game = game.Game(stock, users)
first_move = game.get_first_move()

print(f'Stock pieces: {stock.pieces}')
for usr in users:
    print(f'{usr.user_name} pieces: {usr.user_set}')
print(f'Domino snake: {game.snake}')
print(f'Status: {first_move.user_name.lower()}')
