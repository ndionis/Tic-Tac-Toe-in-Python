# print("Enter cells:", end=" ")
# cells = input()
# table = [
#     [cells[0], cells[1], cells[2]],
#     [cells[3], cells[4], cells[5]],
#     [cells[6], cells[7], cells[8]]
# ]

table = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

enter_coordinates_message = "Enter the coordinates:"


def make_a_move(character):
    print(enter_coordinates_message, end=" ")
    choice = input().split()
    wrong = True
    while wrong:
        if len(choice) != 2 or not choice[0].isdigit() or not choice[1].isdigit():
            print("You should enter numbers!")
            print(enter_coordinates_message, end=" ")
            choice = input().split()

        elif 3 < int(choice[0]) or int(choice[0]) < 1 or \
                int(choice[1]) > 3 or int(choice[1]) < 1:
            print("Coordinates should be from 1 to 3!")
            print(enter_coordinates_message, end=" ")
            choice = input().split()

        elif table[convert_coordinates(choice)[0]][convert_coordinates(choice)[1]] == "X" or \
                table[convert_coordinates(choice)[0]][convert_coordinates(choice)[1]] == "O":
            print("This cell is occupied! Choose another one!")
            print(enter_coordinates_message, end=" ")
            choice = input().split()

        else:
            table[convert_coordinates(choice)[0]][convert_coordinates(choice)[1]] = character
            wrong = False


def play_game(table_cells):
    x_wins = wins(table_cells, "X")  # and not wins(table_cells, "O") and not draw
    o_wins = wins(table_cells, "O")  # and not wins(table_cells, "X") and not draw
    draw = not wins(table_cells, "X") and not wins(table_cells, "O") and number_of_empty_cells(table_cells) == 0

    counter = 0
    while not x_wins and not o_wins and not draw:
        if counter % 2 != 0:
            make_a_move("O")
        else:
            make_a_move("X")

        x_wins = wins(table_cells, "X")
        o_wins = wins(table_cells, "O")
        draw = not wins(table_cells, "X") and not wins(table_cells, "O") and number_of_empty_cells(table_cells) == 0

        print_cells()
        counter += 1

    if x_wins:
        return 1
    elif o_wins:
        return 2
    elif draw:
        return 3


def convert_coordinates(choice):
    if int(choice[0]) == 1 and int(choice[1]) == 3:
        return 0, 0
    elif int(choice[0]) == 2 and int(choice[1]) == 3:
        return 0, 1
    elif int(choice[0]) == 3 and int(choice[1]) == 3:
        return 0, 2
    elif int(choice[0]) == 1 and int(choice[1]) == 2:
        return 1, 0
    elif int(choice[0]) == 2 and int(choice[1]) == 2:
        return 1, 1
    elif int(choice[0]) == 3 and int(choice[1]) == 2:
        return 1, 2
    elif int(choice[0]) == 1 and int(choice[1]) == 1:
        return 2, 0
    elif int(choice[0]) == 2 and int(choice[1]) == 1:
        return 2, 1
    elif int(choice[0]) == 3 and int(choice[1]) == 1:
        return 2, 2


def print_cells():
    print("---------")
    for i in range(0, 3):
        print("|", end=" ")
        for j in range(0, 3):
            print(table[i][j], end=' ')
        print("|")
    print("---------")


def result():
    # winner = game_result(table)
    winner = play_game(table)
    # if 0 == winner:
    #     print("Game not finished")
    if 1 == winner:
        print("X wins")
    elif 2 == winner:
        print("O wins")
    elif 3 == winner:
        print("Draw")
    # elif 4 == winner:
    #     print("Impossible")


# def game_result(table_cells):
#     empties = number_of_empty_cells(table_cells)
#     xs = number_of_cells(table, "X")
#     os = number_of_cells(table, "O")
#     draw = not wins(table_cells, "X") and not wins(table_cells, "O") and number_of_empty_cells(table_cells) == 0
#     x_wins = wins(table_cells, "X") and not wins(table_cells, "O") and not draw
#     o_wins = wins(table_cells, "O") and not wins(table_cells, "X") and not draw
#     impossible = wins(table_cells, "X") and wins(table_cells, "O") or (xs - os >= 2) or (os - xs >= 2)
#     game_not_finished = not draw and not x_wins and not o_wins and not impossible
#
#     if game_not_finished:
#         return 0
#     elif x_wins:
#         return 1
#     elif o_wins:
#         return 2
#     elif draw:
#         return 3
#     elif impossible:
#         return 4


def wins(table_cells, character):
    return (character == table_cells[0][0] and
            character == table_cells[0][1] and
            character == table_cells[0][2]) or \
           (character == table_cells[1][0] and
            character == table_cells[1][1] and
            character == table_cells[1][2]) or \
           (character == table_cells[2][0] and
            character == table_cells[2][1] and
            character == table_cells[2][2]) or \
           (character == table_cells[0][0] and
            character == table_cells[1][0] and
            character == table_cells[2][0]) or \
           (character == table_cells[0][1] and
            character == table_cells[1][1] and
            character == table_cells[2][1]) or \
           (character == table_cells[0][2] and
            character == table_cells[1][2] and
            character == table_cells[2][2]) or \
           (character == table_cells[0][0] and
            character == table_cells[1][1] and
            character == table_cells[2][2]) or \
           (character == table_cells[0][2] and
            character == table_cells[1][1] and
            character == table_cells[2][0])


def number_of_empty_cells(table_cells):
    empty_cells = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if "X" != table_cells[i][j] and "O" != table_cells[i][j]:
                empty_cells += 1

    return empty_cells


def number_of_cells(table_cells, character):
    number_of_cell = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if character == table_cells[i][j]:
                number_of_cell += 1

    return number_of_cell


print_cells()
# make_a_move()
result()
