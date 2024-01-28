import sys


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class Game:
    def __init__(self, players):
        self.board = [" "] * 9
        self.players = players

    def print_board(self):
        for i in range(1, len(self.board) + 1, 3):
            print(' | '.join(self.board[i - 1:i + 2]), "\n---------")

    def check_win(self):
        win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        for condition in win_conditions:
            if all(self.board[i - 1] == self.board[j - 1] == self.board[k - 1] != ' ' for i, j, k in [condition]):
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def get_player_move(self, player):
        while True:
            move = int(input(
                f"Player {player.symbol} - Enter the cell number to place {'X' if player.symbol == 'X' else 'O'} in: \n"))
            if 1 <= move <= 9:
                if self.board[move - 1] == ' ':
                    self.board[move - 1] = player.symbol
                    self.print_board()
                    if self.check_win():
                        print(f"Player {player.symbol} wins!")
                        sys.exit()
                    elif self.check_draw():
                        print("The game is a draw!")
                        sys.exit()
                    return move
                else:
                    print("This cell is already occupied. Please select another cell.")
            else:
                print("Invalid input. Please enter a number from 1 to 9.")

    def play_game(self):
        for _ in range(9):
            self.print_board()
            for player in self.players:
                self.get_player_move(player)
        self.print_board()


player1 = Player('X')
player2 = Player('O')
game = Game([player1, player2])
game.play_game()
