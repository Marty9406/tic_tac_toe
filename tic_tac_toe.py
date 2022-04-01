def print_area():
    for line in area:
        print(AREA_SEPARATOR)
        print('|{:^3}|{:^3}|{:^3}|'.format(*line))
    print(AREA_SEPARATOR)


def choose_player():
    if turn % 2:
        return players[0]
    else:
        return players[1]


def get_next_move(player):
    while True:
        print(TEXT_SEPARATOR)
        number = input('Player {} | Please enter your number: '.format(player))

        if number.isnumeric():
            number = int(number)
        else:
            print('Wrong character!')
            continue

        if 0 < number < 10:
            row = (number - 1) // 3
            column = (number - 1) % 3
        else:
            print('Wrong move!')
            continue

        if players[0] in area[row][column] or players[1] in area[row][column]:
            print('This box is already taken!')
            continue
        else:
            return row, column


def find_winner():
    for player in players:
        for i in win_combinations:
            if [area[i[0]][i[1]], area[i[2]][i[3]], area[i[4]][i[5]]] == [player, player, player]:
                print(TEXT_SEPARATOR)
                print('Congratulations, the player {} won!'.format(player))
                print(TEXT_SEPARATOR)
                exit()


def find_draw():
    if turn == 10:
        print(TEXT_SEPARATOR)
        print('It\'s a draw!')
        print(TEXT_SEPARATOR)
        exit()


AREA_SEPARATOR = '+---+---+---+'
TEXT_SEPARATOR = 45*'='
players = ['O', 'X']
turn = 1

area = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

win_combinations = [
    [0, 0, 0, 1, 0, 2],
    [1, 0, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 2],
    [0, 0, 1, 0, 2, 0],
    [0, 1, 1, 1, 2, 1],
    [0, 2, 1, 2, 2, 2],
    [0, 0, 1, 1, 2, 2],
    [0, 2, 1, 1, 2, 0]
]

print(
    'Welcome to Tic Tac Toe',
    TEXT_SEPARATOR,
    'GAME RULES:',
    'Each player can place one mark (or stone)',
    'per turn on the 3x3 grid. The WINNER is',
    'who succeeds in placing three of their',
    'marks in a: ',
    '- horizontal,',
    '- vertical or',
    '- diagonal row.',
    TEXT_SEPARATOR,
    'Let\'s start the game',
    TEXT_SEPARATOR,
    sep='\n'
)

while True:
    print_area()
    find_winner()
    find_draw()
    chosen_row, chosen_column = get_next_move(choose_player())
    area[chosen_row][chosen_column] = choose_player()
    turn += 1
    print(TEXT_SEPARATOR)
