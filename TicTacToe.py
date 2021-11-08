#STEP 1: Reading the board
def display_board(board):
    row = 0
    col = 0

    arr = [[], [], []]
    for choice in board:
        if col < 3:
            arr[row].append(choice)
            col += 1
        else:
            row += 1
            arr[row].append(choice)
            col = 1

    for i in arr:
        for j in i:
            print("|_{}_|".format(j), end="  "),
        print("\n")




#STEP 2: Obtaining user input
def player_input():
    choice = ''
    while choice != "x" or choice != "o":
        choice = input('Do you want to be X or O? ').lower()

        if choice == "x":
            return ("X", "O")
        elif choice == "o":
            return ("O", "X")
        else:
            print("Incorrect input. Please choose X or O.")
            continue




#STEP 3: Putting marker on the board in desired position
def place_marker(board, marker, position):

    if position == 1 or position == 2 or position == 3:
        board[position + 5] = marker
    elif position == 4 or position == 5 or position == 6:
        board[position-1] = marker
    else:
        board[position-7] = marker




#STEP 4: Checking for a win
def win_check(board, mark):

    #horizontal Check
    if board[0] == mark and board[0] == board[1] and board[0] == board[2]:
        return True
    elif board[3] == mark and board[3] == board[4] and board[3] == board[5]:
        return True
    elif board[6] == mark and board[6] == board[7] and board[6] == board[8]:
        return True



    #Vertical Check
    if board[0] == mark and board[0] == board[3] and board[0] == board[6]:
        return True
    elif board[1] == mark and board[1] == board[4] and board[1] == board[7]:
        return True
    elif board[2] == mark and board[2] == board[5] and board[2] == board[8]:
        return True


    #Diagonal Check
    if board[0] == mark and board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[2] == mark and board[2] == board[4] and board[2] == board[6]:
        return True
    else:
        return False




#STEP 5: Deciding who goes first
import random
def choose_first():
    player = random.randint(1, 2)
    if player == 1:
        print("Player 1 goes first! ")
        return player
    else:
        print("Player 2 goes first!")
        return player




#STEP 6: Returns boolean to see if space is available
def space_check(board, position):
    if position == 1 or position == 2 or position == 3:
        if board[position + 5] == " ":
            return True
    elif position == 4 or position == 5 or position == 6:
        if board[position-1] == " ":
            return True
    elif position == 7 or position == 8 or position == 9:
        if board[position-7] == " ":
            return True
    else:
        return False




#STEP 7: Checks to see if board is full, True = full, false = otherwise
def full_board_check(board):
    for mark in board:
        if mark == " ":
            return False
    return True




#STEP 8: Asking for player position and using step 6 to check if its available
def player_choice(board):
    while True:

        try:
            choice = int(input("Please input the desired position (1-9): "))

        except ValueError:
            print("Incorrect input. Please try again.")
            continue

        if choice < 1 or choice > 9:
            print("Incorrect input. Please try again.")
            continue
        elif not space_check(board, choice):
            print("There is already a piece there. Please input another value.")
            continue
        else:
            return choice




#STEP 9: ask to replay game
def replay():
    answer = ""
    while not answer == "n" or answer == "y":
        answer = input("Do you wish to play again? (Y or N)  ").lower()

        if answer == "y":
            print("\n")
            return True
        if answer == "n":
            return False
        else:
            print("Incorrect input.")
            continue

