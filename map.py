import random


def create_map(rows: int, columns: int) -> dict:
    """
    Create a map of a specified size with assigned values.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be a positive integer larger than or equal to 3
    :postcondition: create a map as a dictionary containing tuples as keys and strings as values;
                    each tuple contains two integers representing row and column in order; center
                    point of the map always associates with a literal value "!" representing the
                    boss; a number (sum of rows and columns) of gridboxes is randomly assigned with
                    "*" as associated values representing the presence of beasts; the rest are
                    assigned with a space character " " as associated values representing nothing is
                    at that location.
    :return: a dictionary representing the map
    """
    game_map = {}
    for row in range(rows):
        for column in range(columns):
            game_map[(row, column)] = " "

    center_point = (int(rows / 2), int(columns / 2))
    game_map[center_point] = "!"

    foe_count = 0
    while foe_count < rows + columns:
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        random_point = (random_row, random_column)
        if random_point != (0, 0) and game_map[random_point] == " ":
            game_map[random_point] = "*"
            foe_count += 1

    return game_map


def print_map(rows: int, columns: int, game_map: dict, character: dict):
    """
    Print the game map.

    :param rows: an integer
    :param columns: an integer
    :param game_map: a dictionary
    :param character: a dictionary
    :precondition: game_map must be a dictionary containing tuples as keys and strings as values,
                   where each tuple contains two integers representing row and column in order;
                   character must be a dictionary containing "current row" and "current column" as
                   keys and their associated values must be integers appearing inside the map
    :postcondition: print the visualized game map

    >>> map_one = {(0, 0): " ", (0, 1): "*", (0, 2): "*", (1, 0): "*", (1, 1): "!", (1, 2): " ", \
                   (2, 0): "*", (2, 1): "*", (2, 2): "*"}
    >>> player_one = {"current row": 0, "current column": 0}
    >>> print_map(3, 3, map_one, player_one)
    <BLANKLINE>
    [@] - You; [*] - Beast; [!] - Dragon
    <BLANKLINE>
    [@][*][*]
    [*][!][ ]
    [*][*][*]
    >>> map_two = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (0, 3): "*", (0, 4): " ", \
                   (1, 0): " ", (1, 1): " ", (1, 2): " ", (1, 3): " ", (1, 4): "*", \
                   (2, 0): " ", (2, 1): " ", (2, 2): "!", (2, 3): " ", (2, 4): "*", \
                   (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): "*", (3, 4): " ", \
                   (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " "}
    >>> player_two = {"current row": 1, "current column": 2}
    >>> print_map(5, 5, map_two, player_two)
    <BLANKLINE>
    [@] - You; [*] - Beast; [!] - Dragon
    <BLANKLINE>
    [ ][ ][ ][*][ ]
    [ ][ ][@][ ][*]
    [ ][ ][!][ ][*]
    [ ][ ][ ][*][ ]
    [ ][ ][ ][ ][ ]
    """
    character_current_location = (character["current row"], character["current column"])
    print("\n[@] - You; [*] - Beast; [!] - Dragon\n")
    for row in range(rows):
        for column in range(columns):
            if (row, column) != character_current_location:
                print(f"[{game_map[(row, column)]}]", end='')
            else:
                print("[@]", end='')
        print()


def clear_foe_on_map(character: dict, game_map: dict):
    """
    Clear the foe on map after beating them.

    :param character: a dictionary
    :param game_map: a dictionary
    :precondition: character must be a dictionary containing "current row" and "current column" as
                   keys and their associated values must be integers appearing inside the game_map;
                   game_map must be a dictionary containing tuples as keys where each tuple contains
                   two integers representing the row and column in order
    :postcondition: change the literal value associated to the character's current position inside
                    the game_map dictionary with a space character " " as a string to represent
                    nothing is there anymore after player beats the foe.

    >>> player_one = {"current row": 0, "current column": 1}
    >>> map_one = {(0, 0): " ", (0, 1): "*", (0, 2): "*", (1, 0): "*", (1, 1): "!", (1, 2): " ", \
                   (2, 0): "*", (2, 1): "*", (2, 2): "*"}
    >>> clear_foe_on_map(player_one, map_one)
    >>> map_one[(0, 1)]
    ' '

    >>> player_two = {"current row": 1, "current column": 1}
    >>> map_two = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (1, 0): " ", (1, 1): "!", (1, 2): " ", \
                   (2, 0): " ", (2, 1): " ", (2, 2): " "}
    >>> clear_foe_on_map(player_two, map_two)
    >>> map_two[(1, 1)]
    ' '
    """
    character_current_location = (character["current row"], character["current column"])
    game_map[character_current_location] = " "
