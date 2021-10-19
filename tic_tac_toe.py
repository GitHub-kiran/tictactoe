    
# PLAY TIC TAC TOE GAME
class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        self.board = [["_"]*3 for _ in range(3)]
    
    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end =" ")
            print()
        print()

    def update_spot(self, row, col, choice):
        self.board[row][col] = choice.upper()

    def is_player_won(self, choice):
        print(self.board)
        choice = choice.upper()
        is_win = None

        # verify whether any row is full
        for i in range(3):
            is_win = True
            for j in range(3):
                if self.board[i][j] != choice:
                    is_win = False
                    break
            if is_win:
                return is_win

        # verify whether any col is full
        for i in range(3):
            is_win = True
            for j in range(3):
                if self.board[j][i] != choice:
                    is_win = False
                    break
            if is_win:
                return is_win

        # verify whether any diagonal is full
        for i in range(3):
            if self.board[i][i] != choice:
                is_win = False
                break
        if is_win:
            return is_win

        for i in range(3):
            if self.board[i][3 - 1 - i] != choice:
                is_win = False
                break
        if is_win:
            return is_win
        return False

    # Verify whether all board is full
    def is_board_filled(self):
        for i in self.board:
            for j in i:
                if j == '_':
                    return False
        return True

    def validate(self, row, col, prev, cur):
        # validate existing entry
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            print("invalid index entered, please try again.")
            return False
        elif self.board[row][col] != "_":
            print("invalid entry, please try again")
            return False
        if not prev:
            return True
        elif prev == cur or cur not in "XxoO":
            print("Wrong player move or wrong choice entered(please use only X/x, O/o symbols)")
            return False
        return True

    def start_game(self):  
        try :     
            # Get players name
            player1 = input("Enter first player name and choice : ") 
            player2 = input("Enter second player name and choice : ")

            # Create 3*3 board filled with "_"
            self.create_board()
            self.display_board()

            # If players name is empty then 'player 1' will be first player and 'player 2' will be second player
            player1 = "Player 1" if not player1 else player1
            player2 = "Player 2" if not player2 else player2
            
            # start with player 1
            # NOTE: in case if player 2 is starting the game, then it should work
            prev_player = player1
            prev_choice = None

            print()
            while True:
                # get user input as row col chioce(ex: 1 2 X)
                row, col, cur_choice = list(
                    map(str, input("Enter row and column in format row col choice : ").split()))
                print()
                
                # validate the inputs, if something is wrong then give 3 retries
                for i in range(1, 4):
                    flag = self.validate(int(row)-1, int(col)-1, prev_choice, cur_choice)
                    if not flag and i < 4:
                        row, col, cur_choice = list(
                        map(str, input("Enter row and column in format row col choice : ").split()))
                    elif flag:
                        break
                    else:
                        print("you have reached max limit of 3 retries, please restart the game")
                        return

                prev_choice = cur_choice

                # update particular spot in the board
                self.update_spot(int(row) - 1, int(col) - 1, cur_choice)

                # Show latest baord
                self.display_board()

                # checking whether current player is won or not
                if self.is_player_won(cur_choice):
                    print("Player {} has won the game!".format(prev_player))
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!!!")
                    break
                prev_player = player1 if prev_player == player1 else player2

            print()

        except:
            print("invalid input")
            return


# start the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()

