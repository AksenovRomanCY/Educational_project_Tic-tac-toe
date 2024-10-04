from gameparts.parts import Board

if __name__ == '__main__':
    game = Board()
    game.display()
    game.make_move(0, 0, 'X')
    print('Ход сделан!')
    game.display()