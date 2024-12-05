def create_character() -> dict:
    """
    Create a beginning character based on user input.

    :postcondition: Create a dictionary which stores basic character information, including user
                    input as name and fixed information like level, current health, current damage,
                    accumulated experience, current row, current column, etc.; print character
                    information once after created
    :return: a dictionary which contains character information

    >>> player_one = create_character() # doctest: +SKIP
    player_one = {"name": "Descartes", "level": 1, "current health": 10, "current damage": 1,
                "base health": 10, "base damage": 1, "accumulated experience": 0, "current row": 0,
                "current column": 0}
    >>> player_two = create_character() # doctest: +SKIP
    player_two = {"name": "Aristotle", "level": 1, "current health": 10, "current damage": 1,
                "base health": 10, "base damage": 1, "accumulated experience": 0, "current row": 0,
                "current column": 0}
    """
    username = input("Welcome to the game, \"One Way Out\"!\n"
                     "Before you start, please tell me your name: ")
    character = {
        "name": username,
        "level": 1,
        "current health": 10,
        "current damage": 1,
        "base health": 10,
        "base damage": 1,
        "accumulated experience": 0,
        "current row": 0,
        "current column": 0
    }
    print(f"\nWelcome again, {username}! Your basic statistics is as follows:\n"
          f"Name: {character['name']}\n"
          f"Level: {character['level']}\n"
          f"HP: {character['current health']}\n"
          f"Damage: {character['current damage']}\n"
          f"Experience: {character['accumulated experience']}")
    return character


def is_alive(character: dict) -> bool:
    """
    Check whether the character is still alive.

    :param character: a dictionary
    :precondition: character must be a dictionary containing a key called "current health"
    :postcondition: Return True if the numeric value corresponded to "current health" key is larger
                    than zero and return False is less than zero
    :return: a boolean where True represents the character is alive and otherwises False

    >>> player_one = {"current health": 5}
    >>> is_alive(player_one)
    True
    >>> player_two = {"current health": 0}
    >>> is_alive(player_two)
    False
    """
    if character["current health"] > 0:
        return True
    else:
        return False


def accumulate_experience(character: dict):
    """
    Add experience to character.

    :param character: a dictionary
    :precondition: character must be a dictionary containing a key, "accumulated experience"
    :postcondition: add a fixed integer, three, to the numeric value corresponded to the
                    "accumulated experience" key inside the character dictionary every time after
                    they beat an enemy
    >>> player_one = {"accumulated experience": 0}
    >>> accumulate_experience(player_one)
    >>> player_one["accumulated experience"]
    3
    >>> player_two = {"accumulated experience": 5}
    >>> accumulate_experience(player_two)
    >>> player_two["accumulated experience"]
    8
    """
    character["accumulated experience"] += 3


def check_if_leve_up(character: dict):
    """
    Check if the character should level up based on their accumulated experience.

    :param character: a dictionary
    :precondition: character must be a dictionary containing several keys, including "name",
                   "accumulated experience", "level", "current health", "base health", "current
                   damage", "base damage"
    :postcondition: Update the character's statistics if numeric value of the character's
                    "accumulated experience" key is larger than or equal to ten or make no changes
                    if it is less than ten; Print the updated character statistics if level up

    >>> player_one = {"name": "Descartes", "level": 1, "current health": 10, "current damage": 1, \
                        "base health": 10, "base damage": 1, "accumulated experience": 0}
    >>> check_if_leve_up(player_one)
    >>> player_one #doctest: +NORMALIZE_WHITESPACE
    {'name': 'Descartes', 'level': 1, 'current health': 10, 'current damage': 1, 'base health': 10,
    'base damage': 1, 'accumulated experience': 0}
    >>> player_two = {"name": "Aristotle", "level": 1, "current health": 1, "current damage": 1, \
                        "base health": 10, "base damage": 1, "accumulated experience": 15}
    >>> check_if_leve_up(player_two)
    <BLANKLINE>
    Level up! Your health is fully recovered, and you can now create higher damage.
    Your basic statistics is as follows:
    Name: Aristotle
    Level: 2
    HP: 20
    Damage: 2
    Experience: 5
    """
    if character["accumulated experience"] >= 10:
        character["level"] += 1
        character["current health"] = character["base health"] * character["level"]
        character["current damage"] = character["base damage"] * character["level"]
        character["accumulated experience"] -= 10
        print("\nLevel up! Your health is fully recovered, and you can now create higher damage.\n"
              "Your basic statistics is as follows:\n"
              f"Name: {character['name']}\n"
              f"Level: {character['level']}\n"
              f"HP: {character['current health']}\n"
              f"Damage: {character['current damage']}\n"
              f"Experience: {character['accumulated experience']}")


def reset_character_position(character: dict):
    """
    Reset the character's current position to the start point.

    :param character: a dictionary
    :precondition: character must be a dictionary containing two keys, "current row" and "current
                   column"
    :postcondition: Change the respective numeric values corresponded to "current row" and "current
                    column" to zero, i.e. the start point (0, 0)

    >>> player_one = {"current row": 5, "current column": 5}
    >>> reset_character_position(player_one)
    >>> (player_one["current row"], player_one["current column"])
    (0, 0)
    >>> player_two = {"current row": 0, "current column": 5}
    >>> reset_character_position(player_two)
    >>> (player_two["current row"], player_two["current column"])
    (0, 0)
    """
    character["current row"] = 0
    character["current column"] = 0
