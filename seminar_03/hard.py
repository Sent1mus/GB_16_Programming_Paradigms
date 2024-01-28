import sys


def print_board(board):
    for i in range(1, len(board) + 1, 3):
        print(' | '.join(board[i - 1:i + 2]), "\n---------")


def check_win(board):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                      (1, 4, 7), (2, 5, 8), (3, 6, 9),
                      (1, 5, 9), (3, 5, 7)]
    for condition in win_conditions:
        if all(board[i - 1] == board[j - 1] == board[k - 1] != ' ' for i, j, k in [condition]):
            return True
    return False


def check_draw(board):
    return ' ' not in board


def get_player_move(board, player):
    while True:
        move = int(input(f"Player {player} - Enter the cell number to place {'X' if player == 1 else 'O'} in: \n"))
        if 1 <= move <= 9:
            if board[move - 1] == ' ':
                board[move - 1] = 'X' if player == 1 else 'O'
                print_board(board)
                if check_win(board):
                    print(f"Player {player} wins!")
                    sys.exit()
                elif check_draw(board):
                    print("The game is a draw!")
                    sys.exit()
                return move
            else:
                print("This cell is already occupied. Please select another cell.")
        else:
            print("Invalid input. Please enter a number from 1 to 9.")


def play_game():
    board = [" "] * 9
    for _ in range(9):
        print_board(board)
        for player in [1, 2]:
            get_player_move(board, player)
    print_board(board)


play_game()
