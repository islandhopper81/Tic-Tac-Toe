from player import Player
import random

class ComputerPlayer(Player):
    def __init__(self, name=None, sign=None, turn=None, level="easy"):
        super().__init__(name, sign, turn)
        self.level = level

    def move(self, board):
        free_cells = board.make_list_of_free_cells()

        index = None
        if self.level == "easy":
            # Easy level: Computer makes a random move
            index = random.choice(free_cells)
        elif self.level == "medium":
            # Medium level: Computer blocks if the opponent is about to win, else makes a random move
            # To Do: Add logic here
            pass
        else:
            # Hard level: Implement a more sophisticated algorithm for computer's move
            # To Do: Add logic here
            pass

        r, c = board.index_to_coords(index)
        board.board[r][c] = self.sign
        return True