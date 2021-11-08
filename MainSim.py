import TicTacToe as ticTac


def Tic_Tac_Toe():
    while True:
        print("Welcome to Tic Tac Toe!")
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ticTac.display_board(board)
        first = ticTac.choose_first()
        marker = ticTac.player_input()

        player = first
        index = 0
        game_on = True
        while game_on:
            print("Player {}'s turn.".format(player))
            position = ticTac.player_choice(board)
            ticTac.place_marker(board, marker[index], position)

            if ticTac.win_check(board, marker[index]):
                print("Player {} wins!".format(player))
                ticTac.display_board(board)
                game_on = False
            elif ticTac.full_board_check(board):
                print("The board is full")
                game_on = False
            else:
                ticTac.display_board(board)
                if player == 1:
                    player = 2
                    if index == 0:
                        index = 1
                    else:
                        index = 0
                else:
                    player = 1
                    if index == 0:
                        index = 1
                    else:
                        index = 0
        if not ticTac.replay():
            break


Tic_Tac_Toe()
