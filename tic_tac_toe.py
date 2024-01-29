from board import Board
from player import Player
from computer_player import ComputerPlayer
import random

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.turn = 1 # User is odd turns
        self.victory = False
        self.player1 = None # this will hold player one
        self.player2 = None # this will hold player two

        # to do: make a game with more than two players


    def check_victory(self, sign):
        # The function analyzes the board's status in order to check if 
        # the player using 'O's or 'X's has won the game
        board = self.board
        
        # first check all the rows to see if they all have the sign
        for r in range(0,len(board.board)):
            if ( all(element == sign for element in board.board[r]) ):
                return True
        
        # now check the columns
        for c in range(0,len(board.board[0])):
            col = [board.board[0][c], board.board[1][c], board.board[2][c]]
            if ( all(element == sign for element in col) ):
                return True
        
        # now check the diaginals
        fwd_index = [1,5,9]
        fwd_diag = [] # this will get populated in the for loop
        for i in fwd_index:
            r,c = board.index_to_coords(i)
            fwd_diag.append(board.board[r][c])
        if ( all(element == sign for element in fwd_diag) ):
            return True
            
        rev_index = [3,5,7]
        rev_diag = [] # this will get populated in the for loop
        for i in rev_index:
            r,c = board.index_to_coords(i)
            rev_diag.append(board.board[r][c])
        if ( all(element == sign for element in rev_diag) ):
            return True
        
        return False

    
    def initalize_players(self):
        # First Player (always the user) #
        name = input("Please enter player 1 name [player1]: ")
        name = "player1" if name == "" else name # set the default if neccessary

        sign = input("Please enter player sign [X]: ")
        sign = "X" if sign == "" else sign # set the default if neccessary

        player1 = Player(name, sign, turn = 1)  # to do: make the turn dynamic
        self.player1 = player1

        # Second Player (another user or computer) #
        player2 = None # initalize here so that I have it in scope later one
        single_player_mode = input("Would you like to play against the computer (Y) or another player (N) [Default: Y]: ")
        if single_player_mode.upper() == "Y" or single_player_mode == "":
            comptuer_sign = "X" if player1.sign == "O" else "O"

            computer_level = input("Please enter the computer's level (easy, medium, hard) [easy]: ")
            computer_level = "easy" if computer_level == "" else computer_level

            player2 = ComputerPlayer("Computer", comptuer_sign, 2, computer_level)
        elif single_player_mode.upper() == "N":
            # create a second player object
            name = input("Please enter player 2 name [player2]: ")
            name = "player2" if name == "" else name # set the default if neccessary

            sign = input("Please enter player sign [O]: ")
            sign = "O" if sign == "" else sign # set the default if neccessary

            # to do: make sure that the signs from players one and two are different

            player2 = Player(name, sign, turn = 2)  # to do: make the turn dynamic
        else:
            print("bad input")

        self.player2 = player2

    def finish_game(self):
        if ( self.turn >= 9 and not self.victory):
            print("Game Over -- Tie!")
        elif ( self.turn % 2 == 0 ):
            print("Game Over -- " + self.player2.name + " Wins!")
        else: 
            print("Game Over -- " + self.player1.name + " Wins!")

    def play(self):
        # Get the information and build player 1
        self.initalize_players()
        player1 = self.player1
        player2 = self.player2

        # To Do: determine the order

        self.board.display()

        while not self.victory:
            # remember I need to make these turns a little more flexible
            sign = None
            if ( self.turn % 2 == 0 ):
                sign = player2.sign
                player2.move(self.board)
            else:
                sign = player1.sign
                player1.move(self.board)
                
            # display the board
            self.board.display()
            
            # check for victory
            self.victory = self.check_victory(sign)
            
            # check for draw
            if ( self.turn >= 9 and not self.victory):
                break # break out of the game without a victor

            if not self.victory:
                self.turn += 1 # go to the next turn 
                
        # finish the game
        self.finish_game()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()