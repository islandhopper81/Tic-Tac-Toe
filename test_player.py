# test_player.py
from player import Player
from board import Board
import pytest

@pytest.fixture
def player_instance():
    # Fixture to create a Player instance for testing
    return Player(name="TestPlayer", sign="X", turn=0)

def test_move_valid_input(player_instance, mocker):
    # Mocking input for valid moves
    test_board = Board()
    mocker.patch('builtins.input', side_effect=["1", "5", "9"])
    
    assert player_instance.move(test_board)
    assert test_board.board[0][0] == "X"

    assert player_instance.move(test_board)
    assert test_board.board[1][1] == "X"

    assert player_instance.move(test_board)
    assert test_board.board[2][2] == "X"

def test_move_invalid_input_then_valid_input(player_instance, mocker):
    # Mocking input for invalid move, then valid move
    test_board = Board()
    mocker.patch('builtins.input', side_effect=["10", "2", "3"])

    # note that in this call to move, 10 is tried first then the user
    # inputs 2 which is a valid move
    assert player_instance.move(test_board)  # Invalid move
    assert test_board.board[0][1] == "X"

    assert player_instance.move(test_board)  # Valid move
    assert test_board.board[0][2] == "X"

def test_wins_incremented(player_instance):
    # Testing if wins are incremented correctly
    assert player_instance.wins == 0
    player_instance.wins += 1
    assert player_instance.wins == 1
