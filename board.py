class Board:
    def __init__(self):
        self.board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

    def display(self):
        # Display the current state of the board
        board_str =  "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "|" + " " * 3 + self.board[0][0] + " " * 3 + "|" + " " * 3 + self.board[0][1] + " " * 3 + "|" + " " * 3 + self.board[0][2] + " " * 3 + "|" + "\n"  # frist row
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
        
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "|" + " " * 3 + self.board[1][0] + " " * 3 + "|" + " " * 3 + self.board[1][1] + " " * 3 + "|" + " " * 3 + self.board[1][2] + " " * 3 + "|" + "\n" # second row
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
        
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "|" + " " * 3 + self.board[2][0] + " " * 3 + "|" + " " * 3 + self.board[2][1] + " " * 3 + "|" + " " * 3 + self.board[2][2] + " " * 3 + "|" + "\n" # third row
        board_str += "|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" + "\n"
        board_str += "+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" + "\n"
        print(board_str)

    def make_list_of_free_cells(self):
        # The function browses the board and builds a list of all the free squares; 
        # the list consists of tuples, while each tuple is a pair of row and column numbers.
        board = self.board

        free_squares = []
        for r in range(0,len(board)):
            for c in range(0,len(board[r])):
                if board[r][c] == "X" or board[r][c] == "O":
                    continue
                free_squares.append(self.coords_to_index(r,c))
        
        return free_squares

    def coords_to_index(self, row, col):
        # Convert coordinates to index
        # this assumes a 3x3 board
        return row * 3 + col + 1

    def index_to_coords(self, index):
        # Convert index to coordinates
        # this assumes a 3x3 board
        row = (index - 1) // 3
        col = (index - 1) % 3
        return row,col

    def update_board(self, index, sign):
        # Update the board with the player's move
        # not sure what I need to put here
        return False