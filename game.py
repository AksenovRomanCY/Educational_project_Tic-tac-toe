from gameparts.parts import Board


def main():
    game = Board()
    game.display()
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
