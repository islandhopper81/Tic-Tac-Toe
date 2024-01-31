from input_validator import InputValidator
import pytest

@pytest.mark.parametrize(
    "sign, used_signs, expected_sign, expected_exception, error_message", 
    [
        ("X", ["O"], "X", None, None),
        ("X", [], "X", None, None),
        ("X", ["X"], None, ValueError, "That sign is already being used by another player"),
        ("1", [], None, ValueError, "Player sign must NOT be an integer between 1 and 9"),
        (1, [], None, ValueError, "Player sign must be a string"),
    ])
def test_validate_sign(sign, used_signs, expected_sign, expected_exception, error_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=error_message):
            InputValidator.validate_sign(sign, used_signs)
    else:
        assert InputValidator.validate_sign(sign, used_signs) == expected_sign
    
@pytest.mark.parametrize(
    "mode, expected_mode, expected_exception, error_message",
    [
        ("C", "C", None, None),
        ("P", "P", None, None),
        (1, None, ValueError, "Game modes must be either C or P"),
        ("X", None, ValueError, "Game modes must be either C or P"),
    ]
)
def test_validate_game_mode(mode, expected_mode, expected_exception, error_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=error_message):
            InputValidator.validate_game_mode(mode)
    else:
        assert InputValidator.validate_game_mode(mode) == expected_mode

@pytest.mark.parametrize(
    "level, expected_level, expected_exception, error_message",
    [
        ("easy", "easy", None, None),
        ("blah", None, ValueError, "Difficulty level must be either easy, medium, or hard"),
        (1, None, ValueError, "Difficulty level must be either easy, medium, or hard"),
    ]
)
def test_validate_level(level, expected_level, expected_exception, error_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=error_message):
            InputValidator.validate_level(level)
    else:
        assert InputValidator.validate_level(level) == expected_level

@pytest.mark.parametrize(
    "turn, expected_turn, expected_exception, error_message",
    [
        (1, 1, None, None),
        (2, 2, None, None),
        ("a", None, ValueError, "turn must be either 1 or 2"),
        (10, None, ValueError, "turn must be either 1 or 2"),
    ]
)
def test_validate_turn(turn, expected_turn, expected_exception, error_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=error_message):
            InputValidator.validate_turn(turn)
    else:
        assert InputValidator.validate_turn(turn) == expected_turn

