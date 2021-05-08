import stock
import user
import game


stock = stock.Stock()
ai_user = user.User('Computer', stock)
human_user = user.User('Player', stock)
game = game.Game(stock, ai_user, human_user)
player = game.get_first_move()
while True:
    game.print_situation()
    result = game.make_turn(player)
    if result == 'Continue':
        player = game.change_player(player)
    else:
        game.print_situation()
        break
