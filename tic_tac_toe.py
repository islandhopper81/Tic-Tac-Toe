from board import Board
from player import Player
from computer_player import ComputerPlayer
from input_validator import InputValidator
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


    def create_human_player(self, default_name, default_sign, turn, used_signs=None):
        # get the users name
        name = input("Please enter player name [" + default_name + "]: ")
        name = default_name if name == "" else name # set default if necessary

        # get the users sign
        sign = None
        while sign is None:
            sign = input("Please enter " + name + "'s sign [" + default_sign + "]: ")
            sign = default_sign if sign == "" else sign # set default if necessary
            try: 
                sign = InputValidator.validate_sign(sign, used_signs)
            except ValueError as e:   
                print(f"Error: {e}. Please enter a different sign.")
                sign = None

        
        player = Player(name=name, sign=sign, turn= turn)
        return(player)

    
    def create_computer_player(self, used_signs=None):
        name = "Computer"
        sign = "O" if "X" in used_signs else "O"
        turn = 2

        # get the level of difficulty
        level = None
        while level is None:
            level = input("What level of difficulty would you prefer: easy, medium, hard [easy]: ")
            level = "easy" if level == "" else level # set default if necessary
            try:
                level = InputValidator.validate_level(level)
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid level.")
                level = None

        player = ComputerPlayer(name, sign, turn, level)
        return(player)


    def get_game_mode(self):
        single_player_mode = True
        game_mode = None
        while game_mode is None:
            game_mode = input("Would you like to play against the computer (C) or another player (P) [Default: C]: ")
            game_mode = "C" if game_mode == "" else game_mode # set default if necessary
            game_mode = game_mode.upper()
            
            try:
                game_mode = InputValidator.validate_game_mode(game_mode)
            except ValueError as e:
                print(f"Error {e}. Please enter a valid mode.")
                game_mode = None
            
            if game_mode == "P":
                single_player_mode = False
                
        return(single_player_mode)

    
    def initalize_players(self):
        # First Player (always the user) #
        self.player1 = self.create_human_player("player1", "X", 1, [])

        # Get the game mode.  Users can either play against the computer or another user.
        # When playing against the computer the get_game_mode will return True
        single_player_mode = self.get_game_mode()        

        # set up the second player -- computer or another user
        if single_player_mode:
            self.player2 = self.create_computer_player([self.player1.sign])
        else:
            self.player2 = self.create_human_player("player2", "O", 2, [self.player1.sign])


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

        # To Do: determine the turn order

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