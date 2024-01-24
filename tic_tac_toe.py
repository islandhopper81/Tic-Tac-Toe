import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board_str =  "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "|" + " " * 3 + board[0][0] + " " * 3 + "|" + " " * 3 + board[0][1] + " " * 3 + "|" + " " * 3 + board[0][2] + " " * 3 + "|" + "\n"  # frist row
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
    
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "|" + " " * 3 + board[1][0] + " " * 3 + "|" + " " * 3 + board[1][1] + " " * 3 + "|" + " " * 3 + board[1][2] + " " * 3 + "|" + "\n" # second row
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
    
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "|" + " " * 3 + board[2][0] + " " * 3 + "|" + " " * 3 + board[2][1] + " " * 3 + "|" + " " * 3 + board[2][2] + " " * 3 + "|" + "\n" # third row
    board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
    board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+"
    print(board_str)
    
def user_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_cells = make_list_of_free_cells(board)
    index = int(input("Enter your move: "))
    
    while index not in free_cells:
        print(index)
        print(free_cells)
        print(index in free_cells)
        print(type(index))
        print(type(free_cells[0]))
        
        print("That is not a valid move")
        index = int(input("Enter your move: "))

    r,c = index_to_coords(index)
    board[r][c] = "O"
    return True


def make_list_of_free_cells(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for r in range(0,len(board)):
        for c in range(0,len(board[r])):
            if board[r][c] == "X" or board[r][c] == "O":
                continue
            free_squares.append(coords_to_index(r,c))
    
    return free_squares
    
def coords_to_index(row, col):
    return row * 3 + col + 1
    
def index_to_coords(index):
    row = (index - 1) // 3
    col = (index - 1) % 3
    return row,col


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    return True


def computer_move(board):
    # The function draws the computer's move and updates the board.
    free_cells = make_list_of_free_cells(board)
    index = random.choice(free_cells)
    r,c = index_to_coords(index)
    board[r][c] = "X"
    return True


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # first check all the rows to see if they all have the sign
    for r in range(0,len(board)):
        if ( all(element == sign for element in board[r]) ):
            return True
    
    # now check the columns
    for c in range(0,len(board[0])):
        col = [board[0][c], board[1][c], board[2][c]]
        if ( all(element == sign for element in col) ):
            return True
    
    # now check the diaginals
    fwd_index = [1,5,9]
    fwd_diag = []
    for i in fwd_index:
        r,c = index_to_coords(i)
        fwd_diag.append(board[r][c])
    if ( all(element == sign for element in fwd_diag) ):
        return True
        
    rev_index = [3,5,7]
    rev_diag = []
    for i in rev_index:
        r,c = index_to_coords(i)
        rev_diag.append(board[r][c])
    if ( all(element == sign for element in rev_diag) ):
        return True
    
    return False
    
board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]

turn = 1 # user is odd turns
victory = False

display_board(board)

while victory == False:
    if ( turn % 2 == 0 ):
        sign = "X"
        computer_move(board)
    else:
        sign = "O"
        user_move(board)
        
    # display the board
    display_board(board)
    
    # check for victory
    victory = victory_for(board, sign)
    
    # check for draw
    if ( turn >= 8 and not victory):
        break # break out of the game without a victor

    if not victory:
        turn += 1 # go to the next turn 
        
# finish the game
if ( turn >= 8 and not victory):
    print("Gamve Over -- Tie!")
elif ( turn % 2 == 0 ):
    print("Game Over -- You Lose!")
else: 
    print("Game Over -- You Win!")


