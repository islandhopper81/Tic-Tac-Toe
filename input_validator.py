class InputValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_sign(sign, used_signs=[]):
        if not isinstance(used_signs, list):
            raise ValueError("used_signs must be a list.  I can be an empty list.")
        if not isinstance(sign, str):
            raise ValueError("Player sign must be a string")
        if sign.isdigit() and 1 <= int(sign) <= 9:
            raise ValueError("Player sign must NOT be an integer between 1 and 9")
        if sign in used_signs:
            raise ValueError("That sign is already being used by another player")
        
        return(sign)

    @staticmethod
    def validate_game_mode(game_mode):
        # the C mode means the user is playing against the computer
        # the P mode means the user is playing against another user
        valid_modes = ["C", "P"]
        if not game_mode in valid_modes:
            raise ValueError("Game modes must be either C or P")

        return(game_mode)

    @staticmethod
    def validate_level(level):
        valid_levels = ["easy", "medium", "hard"]
        if not level in valid_levels:
            raise ValueError("Difficulty level must be either easy, medium, or hard")

        return(level)

    @staticmethod
    def validate_turn(turn):
        # to do: do I really need this method.  This check might actually go better in 
        # the player class or simply in the main when I generate the turn.
        valid_turns = [1,2]
        if not turn in valid_turns:
            raise ValueError("turn must be either 1 or 2")

        return(turn)
        
