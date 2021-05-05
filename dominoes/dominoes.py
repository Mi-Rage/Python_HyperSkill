import stock
import user
import game


stock = stock.Stock()
users = [user.User('Computer', stock), user.User('Player', stock)]
game = game.Game(stock, users)
game.get_first_move()
game.print_situation()
