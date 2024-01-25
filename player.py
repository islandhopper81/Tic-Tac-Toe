class Player:
    def __init__(self, name=None, sign=None, turn=None):
        self.name = name
        self.sign = sign
        self.wins = 0
        self.turn = turn

    def move(self, board):
        free_cells = board.make_list_of_free_cells()
        cell_index = int(input(f"{self.name}, enter your move: "))

        while cell_index not in free_cells:
            print("That is not a valid move")
            cell_index = int(input(f"{self.name}, enter your move: "))

        r, c = board.index_to_coords(cell_index)
        board.board[r][c] = self.sign
        return True
