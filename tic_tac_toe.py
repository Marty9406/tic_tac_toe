def print_field():
    for row in field:
        print(FIELD_SEPARATOR)
        print("|{:^3}|{:^3}|{:^3}|".format(*row))
    print(FIELD_SEPARATOR)


def choose_player():
    if turn % 2:
        return "o"
    else:
        return "x"


def get_move_number(player):
    while True:
        print(TEXT_SEPARATOR_DOUBLE)
        number = input("Player {} | Please enter your number:".format(player))
        if number.isnumeric():
            number = int(number)
            if 0 < number < 10:
                row = (number - 1) // 3
                column = (number - 1) % 3
                if "X" in field[row][column] or "O" in field[row][column]:
                    print("This box is already taken!")
                    continue
                else:
                    return row, column
            else:
                print("Wrong move!")
                continue
        else:
            print("Wrong character!")
            continue


def winner_control():
    for player in ["X", "O"]:
        if field[0][0] == player and field[0][1] == player and field[0][2] == player\
        or field[1][0] == player and field[1][1] == player and field[1][2] == player\
        or field[2][0] == player and field[2][1] == player and field[2][2] == player\
        or field[0][0] == player and field[1][0] == player and field[2][0] == player\
        or field[0][1] == player and field[1][1] == player and field[2][1] == player\
        or field[0][2] == player and field[1][2] == player and field[2][2] == player\
        or field[0][0] == player and field[1][1] == player and field[2][2] == player\
        or field[0][2] == player and field[1][1] == player and field[2][0] == player:
            print(TEXT_SEPARATOR_DOUBLE)
            print("Congratulations, the player {} won!".format(player))
            print(TEXT_SEPARATOR_DOUBLE)
            exit()


field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
         ]
FIELD_SEPARATOR = "+---+---+---+"
TEXT_SEPARATOR_DOUBLE = 45*"="
TEXT_SEPARATOR_SIMPLE = 45*"-"
turn = 1

print(
    "Welcome to Tic Tac Toe",
    TEXT_SEPARATOR_DOUBLE,
    "GAME RULES:",
    "Each player can place one mark (or stone)",
    "per turn on the 3x3 grid. The WINNER is",
    "who succeds in placing three of their",
    "marks in a: ",
    "- horizontal,",
    "- vertical or",
    "- diagonal row.",
    TEXT_SEPARATOR_DOUBLE,
    "Let's start the game",
    TEXT_SEPARATOR_SIMPLE,
    sep="\n"
      )

while True:
    print_field()
    winner_control()
    if turn == 10:
        print("It's a draw!")
        break
    row, column = get_move_number(choose_player())
    player = choose_player()
    field[row][column] = player.upper()
    turn += 1
    print(TEXT_SEPARATOR_DOUBLE)

