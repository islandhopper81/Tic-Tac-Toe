import pytest
from board import Board

@pytest.fixture
def empty_board():
    return Board()

def test_display(empty_board, capsys):
    empty_board.display()
    captured = capsys.readouterr()
    expected_output = (
        "+-------+-------+-------+\n"
        "|       |       |       |\n"
        "|   1   |   2   |   3   |\n"
        "|       |       |       |\n"
        "+-------+-------+-------+\n"
        "|       |       |       |\n"
        "|   4   |   5   |   6   |\n"
        "|       |       |       |\n"
        "+-------+-------+-------+\n"
        "|       |       |       |\n"
        "|   7   |   8   |   9   |\n"
        "|       |       |       |\n"
        "+-------+-------+-------+\n\n"
    )
    assert captured.out == expected_output

def test_make_list_of_free_cells(empty_board):
    # Test when the board is empty
    free_cells = empty_board.make_list_of_free_cells()
    expected_free_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert free_cells == expected_free_cells

    # Test when some cells are already marked
    empty_board.board[0][0] = "X"
    empty_board.board[1][1] = "O"
    free_cells = empty_board.make_list_of_free_cells()
    expected_free_cells = [2, 3, 4, 6, 7, 8, 9]
    assert free_cells == expected_free_cells

def test_coords_to_index(empty_board):
    assert empty_board.coords_to_index(0, 0) == 1
    assert empty_board.coords_to_index(1, 2) == 6
    assert empty_board.coords_to_index(2, 2) == 9

def test_index_to_coords(empty_board):
    assert empty_board.index_to_coords(1) == (0, 0)
    assert empty_board.index_to_coords(6) == (1, 2)
    assert empty_board.index_to_coords(9) == (2, 2)
