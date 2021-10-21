    
# PLAY TIC TAC TOE GAME
# NOTE: compatible on python 3+ version

import random
class TicTacToe:
    def __init__(self):
        self.board = []
        self.idx = 3

    # create the board
    def create_board(self):
        self.board = [["_"]*3 for _ in range(3)]
    
    # show the board
    def display_board(self):
        for i in range(self.idx):
            for j in range(self.idx):
                print(self.board[i][j], end =" ")
            print()
        print()

    # update the spot with provided symbol
    def update_spot(self, row, col, choice):
        self.board[row][col] = choice.upper()

    def is_player_won(self, choice):
        import pdb 
        choice = choice.upper()
        is_win = None

        # verify whether any row is full
        for i in range(self.idx):
            is_win = True
            for j in range(self.idx):
                if self.board[i][j] != choice:
                    is_win = False
                    break
            if is_win:
                return is_win

        # verify whether any col is full
        for i in range(self.idx):
            is_win = True
            for j in range(self.idx):
                if self.board[j][i] != choice:
                    is_win = False
                    break
            if is_win:
                return is_win

        # verify whether any diagonal is full
        is_win = True
        for i in range(self.idx):
            if self.board[i][i] != choice:
                is_win = False
                break
        if is_win:
            return is_win

        is_win = True
        for i in range(self.idx):
            if self.board[i][self.idx - 1 - i] != choice:
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
        # validate the index, row/col index is less than 0 or more than 2 is not accepted
        if (row < 0 or row > self.idx-1) or (col < 0 or col > self.idx-1):
            print("invalid index entered, please try again.")
            return False
        # verify whether index is already filled
        elif self.board[row][col] != "_":
            print("invalid entry, please try again")
            return False
        # verify consecutive same symbol and invalid symbol
        if prev == cur or cur not in "XxoO":
            print("Wrong player move or wrong choice entered(please use only X/x, O/o symbols)")
            return False
        return True


    # start point 
    def start(self):
        # Create 3*3 board filled with "_"
        self.create_board()
        self.display_board()
    
    def play_against_friend(self):  
        try :     
            # Get players name
            player1 = input("Enter first player name : ") 
            player2 = input("Enter second player name : ")

            # If players name is empty then 'player 1' will be first player and 'player 2' will be second player
            player1 = "Player 1" if not player1 else player1
            player2 = "Player 2" if not player2 else player2
            
            # create and display the board
            self.start()

            # start with random player
            prev_player = None
            prev_choice = None
            print()

            while True:
                # get user input as row col chioce(ex: 1 2 X)
                row, col, cur_choice = list(
                    map(str, input("Enter row and column in format row col choice : ").split()))
                print()
                
                # validate the inputs, if input is wrong then give 3 retries
                max_try = 4
                for i in range(1, max_try):
                    flag = self.validate(int(row)-1, int(col)-1, prev_choice, cur_choice)
                    if not flag and i < 4:
                        row, col, cur_choice = list(
                        map(str, input("Enter row and column in format row col choice : ").split()))
                    elif flag:
                        break   
                    else:
                        print("you have reached max limit of 3 retries, please restart the game")
                        return
                        # [TODO] : option to restart the game 
                        # restart = input("do you want to restart the game, type Y/N ?")
                        # if restart.upper() == "Y":
                        #     self.play_against_friend()
                        # else:
                        #     return 

                prev_choice = cur_choice

                # update particular spot in the board
                self.update_spot(int(row) - 1, int(col) - 1, cur_choice)

                # Show latest baord
                self.display_board()

                # checking whether current player is won or not
                if prev_player and self.is_player_won(cur_choice):
                    prev_player = player2 if prev_player == player1 else player1
                    print("Player {} has won the game!".format(prev_player))
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!!!")
                    break
                # swap the player
                prev_player = player2 if prev_player == player1 else player1

            # adjust with new line
            print()

        except:
            print("invalid input provided, please restart the game!")

    def play_against_computer(self):
        try:
            # Get player name
            player1 = input("Enter first player name : ") 
            player1 = "Player 1" if not player1 else player1
            player2 = "computer"

            # create and display the board
            self.start()

            # start with random player
            prev_player = None
            prev_choice = None
            print()
            random_moves = [(i,j) for i in range(1,4) for j in range(1,4)]

            while True:
                # get user input as row col chioce(ex: 1 2 X)
                if not prev_player or prev_player is not player1:
                    row, col, cur_choice = list(
                        map(str, input("Enter row and column in format row col choice : ").split()))
                    print()
                    if (int(row), int(col)) in random_moves:
                        del random_moves[random_moves.index((int(row), int(col)))]
                else:
                    move = random_moves.pop(random.randrange(len(random_moves)))
                    row, col = move[1], move[0]
                    cur_choice = "X" if prev_choice in "Oo" else "O"
                
                # validate the inputs, if input is wrong then give 3 retries
                if not prev_player or prev_player is not player1:

                    max_try = 4
                    for i in range(1, max_try):
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
                if prev_player and self.is_player_won(cur_choice):
                    prev_player = player2 if prev_player == player1 else player1
                    print("Player {} has won the game!".format(prev_player))
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!!!")
                    break
                # swap the player
                prev_player = player2 if prev_player == player1 else player1

            # adjust with new line
            print()

        except:
            print("invalid input provided, please restart the game!")
            raise


# start the game
tic_tac_toe = TicTacToe()
play_option = input("Do you want to play with computer, type Y/Yes ? ")
if play_option.upper() == "Y" or play_option.upper() == "YES":
    tic_tac_toe.play_against_computer()
else:
    tic_tac_toe.play_against_friend()



