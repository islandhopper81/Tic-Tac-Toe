import pytest
from tic_tac_toe import TicTacToe

@pytest.mark.parametrize("inputs, expected_name, expected_sign, expected_level", [
    (['', '', '', ''], 'Computer', 'O', 'easy'),
    (['player1', 'X', 'N', 'player2', 'O'], 'player2', 'O', None)
])
def test_initialize_players(inputs, expected_name, expected_sign, expected_level, monkeypatch, capsys):
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    game = TicTacToe()
    game.initalize_players()

    assert game.player1.name == 'player1'
    assert game.player1.sign == 'X'
    
    assert game.player2.name == expected_name
    assert game.player2.sign == expected_sign
    assert getattr(game.player2, 'level', None) == expected_level

def test_check_victory_horizontal():
    game = TicTacToe()
    game.board.board = [['X', 'X', 'X'],
                        ['O', 'O', 6],
                        [7, 8, 9]]
    result = game.check_victory('X')
    assert result

def test_check_victory_vertical():
    game = TicTacToe()
    game.board.board = [['X', 'O', 2],
                        ['X', 'O', 5],
                        ['X', 7, 8]]
    result = game.check_victory('X')
    assert result

def test_check_victory_fwd_diagonal():
    game = TicTacToe()
    game.board.board = [['X', 'O', 2],
                        ['O', 'X', 5],
                        [6, 7, 'X']]
    result = game.check_victory('X')
    assert result

def test_check_victory_rev_diagonal():
    game = TicTacToe()
    game.board.board = [[1, 'O', 'X'],
                        ['O', 'X', 5],
                        ['X', 7, 8]]
    result = game.check_victory('X')
    assert result

def test_play_game_tie(monkeypatch, capsys):
    inputs = ['player1', 'X', 'N', 'player2', 'O', '1', '2', '3', '5', '4', '6', '8', '7', '9']
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))

    game = TicTacToe()
    game.play()

    captured = capsys.readouterr()
    lines = captured.out.splitlines()  # I only really care about the last line
    assert lines[-1] == "Game Over -- Tie!"

def test_play_game_player1_wins(monkeypatch, capsys):
    inputs = ['player1', 'X', 'N', 'player2', 'O', '1', '2', '3', '4', '5', '6', '7']
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))

    game = TicTacToe()
    game.play()

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[-1] == "Game Over -- player1 Wins!"

def test_play_game_player2_wins(monkeypatch, capsys):
    inputs = ['player1', 'X', 'N', 'player2', 'O', '2', '1', '3', '4', '5', '7']
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))

    game = TicTacToe()
    game.play()

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[-1] == "Game Over -- player2 Wins!"

