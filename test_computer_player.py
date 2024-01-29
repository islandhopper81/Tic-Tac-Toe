# test_computer_player.py
import pytest
from player import Player
from computer_player import ComputerPlayer
from board import Board

@pytest.fixture
def computer_player_instance():
    return ComputerPlayer(name="Computer", sign="X", turn=1, level="easy")

def test_computer_player_creation(computer_player_instance):
    assert computer_player_instance.name == "Computer"
    assert computer_player_instance.sign == "X"
    assert computer_player_instance.turn == 1
    assert computer_player_instance.level == "easy"

def test_easy_level_move(computer_player_instance, mocker):
    # Mocking random.choice to always return a specific value (5 in this case)
    mocker.patch('random.choice', return_value=5)

    # Mocking the board and its methods
    test_board = Board()

    # Call the move method
    assert computer_player_instance.move(test_board)

    # Ensure that the move is applied to the board
    assert test_board.board[1][1] == "X"


# Add more test cases for "medium" and "hard" levels as needed

