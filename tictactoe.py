# # write your code here
# print("X O X")
# print("X O X")
# print("X O X")
def print_grid(grid_list):
    print("---------")
    print("| " + " ".join(grid_list[0:3]) + " |")
    print("| " + " ".join(grid_list[3:6]) + " |")
    print("| " + " ".join(grid_list[6:9]) + " |")
    print("---------")


def enter_and_check_coordinates(grid_list, _last_symbol):
    # Prompt the user to make a move.
    coordinate = input("Enter the coordinates:")
    # The user should input 2 numbers that represent the cell where they want to place their X.
    coordinate_list = coordinate.split()
    # Analyze user input and show messages in the following situations:
    # If the user enters something other than 2 numbers
    if len(coordinate_list) != 2:
        print("You should enter numbers!")
        enter_and_check_coordinates(grid_list, _last_symbol)
    elif not (coordinate_list[0].isnumeric() and coordinate_list[1].isnumeric()):
        print("You should enter numbers!")
        enter_and_check_coordinates(grid_list, _last_symbol)
    else:
        first_coordinate_int = int(coordinate_list[0])
        second_coordinate_int = int(coordinate_list[1])
        # If the user enters a number that is not between 1 and 3
        if first_coordinate_int < 1 or first_coordinate_int > 3 or second_coordinate_int < 1 or second_coordinate_int > 3:
            print("Coordinates should be from 1 to 3!")
            enter_and_check_coordinates(grid_list, _last_symbol)
        # If the user enters a number that is already occupied
        elif grid_list[coordinate_to_index(first_coordinate_int, second_coordinate_int)] != "_":
            # print(coordinate_to_index(first_coordinate_int, second_coordinate_int))
            print("This cell is occupied! Choose another one!")
            # print(grid_list[coordinate_to_index(first_coordinate_int, second_coordinate_int)])
            enter_and_check_coordinates(grid_list, _last_symbol)
        # Update the grid to include the user's move
        else:
            grid_list[coordinate_to_index(first_coordinate_int, second_coordinate_int)] = _last_symbol
            global symbols_list
            symbols_list = grid_list


def coordinate_to_index(x, y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 and y == 2:
        return 1
    elif x == 1 and y == 3:
        return 2
    elif x == 2 and y == 1:
        return 3
    elif x == 2 and y == 2:
        return 4
    elif x == 2 and y == 3:
        return 5
    elif x == 3 and y == 1:
        return 6
    elif x == 3 and y == 2:
        return 7
    elif x == 3 and y == 3:
        return 8


# Get the 3x3 grid from the input as in the previous stages.
# symbols = input("Enter cells:")
symbols = "_________"
symbols_list = list(symbols)
# Output this 3x3 grid as in the previous stages.
print_grid(symbols_list)
last_symbol = "X"
while True:
    enter_and_check_coordinates(symbols_list, last_symbol)
    # print the updated grid to the console
    print_grid(symbols_list)
    # If the user wins, show the message "XXX wins".
    string = ""
    for i in range(1, 20, 4):
        string += "&" * i
    oWins = False
    xWins = False
    draw = False
    winSymbol = ""
    if symbols_list[0] == symbols_list[1] == symbols_list[2]:
        winSymbol = symbols_list[0]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[3] == symbols_list[4] == symbols_list[5]:
        winSymbol = symbols_list[3]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[6] == symbols_list[7] == symbols_list[8]:
        winSymbol = symbols_list[6]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[0] == symbols_list[3] == symbols_list[6]:
        winSymbol = symbols_list[0]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[1] == symbols_list[4] == symbols_list[7]:
        winSymbol = symbols_list[1]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[2] == symbols_list[5] == symbols_list[8]:
        winSymbol = symbols_list[2]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[0] == symbols_list[4] == symbols_list[8]:
        winSymbol = symbols_list[0]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    if symbols_list[2] == symbols_list[4] == symbols_list[6]:
        winSymbol = symbols_list[2]
        if winSymbol == "X":
            xWins = True
        elif winSymbol == "O":
            oWins = True
    else:
        draw = True
    xCount = symbols_list.count("X")
    oCount = symbols_list.count("O")
    if last_symbol == "X":
        last_symbol = "O"
    elif last_symbol == "O":
        last_symbol = "X"
    if xWins and oWins:
        print("Impossible")
    elif xCount - oCount > 1 or oCount - xCount > 1:
        print("Impossible")
    elif xWins:
        print("X wins")
        break
    elif oWins:
        print("O wins")
        break
    elif symbols_list.count("_") > 0:
        print("Game not finished")
    elif draw:
        print("Draw")
        break
