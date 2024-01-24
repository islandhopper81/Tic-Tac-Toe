from board import Board
import random

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.turn = 1 # User is odd turns
        self.victory = False


    def user_move(self):
        # The function accepts the board's current status, asks the user about their move, 
        # checks the input, and updates the board according to the user's decision.
        board = self.board

        free_cells = board.make_list_of_free_cells()
        index = int(input("Enter your move: "))
        
        while index not in free_cells:
            print("That is not a valid move")
            index = int(input("Enter your move: "))

        r,c = board.index_to_coords(index)
        board.board[r][c] = "O"
        return True


    def computer_move(self):
        # The function draws the computer's move and updates the board.
        board = self.board

        free_cells = board.make_list_of_free_cells()
        index = random.choice(free_cells)
        r,c = board.index_to_coords(index)
        board.board[r][c] = "X"
        return True


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

    def play(self):
        self.board.display()

        while not self.victory:
            if ( self.turn % 2 == 0 ):
                sign = "X"
                self.computer_move()
            else:
                sign = "O"
                self.user_move()
                
            # display the board
            self.board.display()
            
            # check for victory
            self.victory = self.check_victory(sign)
            
            # check for draw
            if ( self.turn >= 8 and not self.victory):
                break # break out of the game without a victor

            if not self.victory:
                self.turn += 1 # go to the next turn 
                
        # finish the game
        if ( self.turn >= 8 and not self.victory):
            print("Gamve Over -- Tie!")
        elif ( self.turn % 2 == 0 ):
            print("Game Over -- You Lose!")
        else: 
            print("Game Over -- You Win!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()