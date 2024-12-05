def get_direction() -> str:
    """
    Ask player to input the direction that they want to move to.

    :postcondition: get user input for their desired direction, and return their desired direction
                    either "W", "A", "S", "D" or "QUIT" in all caps as a string
    :return: a string specifying the desired direction
    """
    direction = input("Enter \"W-A-S-D\" to move up-left-down-right or \"Quit\" to quit the game: ")
    direction = direction.upper()
    valid_input = ["W", "A", "S", "D", "QUIT"]
    if direction not in valid_input:
        print("Invalid input! Please try again.\n")
        direction = get_direction()
    return direction


def validate_move(direction: str, character: dict[str, int], game_map: dict[tuple, str]) -> bool:
    """
    Validate the desired direction inputted by player.

    :param direction: a string
    :param character: a dictionary
    :param game_map: a dictionary
    :precondition: direction must be a string which is either "W", "A", "S" or "D"; character must
                   be a dictionary containing the two keys "current row" and "current column";
                   game_map must be a well-formed containing valid location as tuples where each
                   tuple contain two integers representing row and column
    :postcondition: validate direction to ensure the player's desired direction in each move is
                    valid, i.e. the row and column that the player wants to move forward to exists
                    in the game_map dictionary as a tuple
    :return: a Boolean where True represents a valid move and False represents an invalid move

    >>> player_one = {"current row": 0, "current column": 0}
    >>> map_one = {(0, 0): " ", (0, 1): " ", (1, 0): "!", (1, 1): "*"}
    >>> validate_move("W", player_one, map_one)
    <BLANKLINE>
    Warning! You're heading to a wrong way. Please enter a valid direction.
    False
    >>> player_two = {"current row": 0, "current column": 0}
    >>> map_two = {(0, 0): " ", (0, 1): " ", (1, 0): "!", (1, 1): "*"}
    >>> validate_move("S", player_two, map_two)
    True
    """
    destination_row = character["current row"]
    destination_column = character["current column"]

    if direction == "W":
        destination_row -= 1
    if direction == "S":
        destination_row += 1
    if direction == "A":
        destination_column -= 1
    if direction == "D":
        destination_column += 1

    if (destination_row, destination_column) in game_map:
        return True
    else:
        print("\nWarning! You're heading to a wrong way. Please enter a valid direction.")
        return False


def move_character(direction: str, character: dict[str, int]):
    """
    Move the character to the player's desired direction.

    :param direction: a string
    :param character: a dictionary
    :precondition: direction must be a string which is either "W", "A", "S" or "D"; character must
                   be a dictionary containing the two keys, "current row" and "current column"
    :postcondition: update the value associated with either the "current row" or "current column"
                    key inside the character dictionary

    >>> player_one = {"current row": 0, "current column": 0}
    >>> move_character("S", player_one)
    >>> player_one
    {'current row': 1, 'current column': 0}
    >>> player_two = {"current row": 2, "current column": 2}
    >>> move_character("D", player_two)
    >>> player_two
    {'current row': 2, 'current column': 3}
    """
    if direction == "W":
        character["current row"] -= 1
    if direction == "S":
        character["current row"] += 1
    if direction == "A":
        character["current column"] -= 1
    if direction == "D":
        character["current column"] += 1
