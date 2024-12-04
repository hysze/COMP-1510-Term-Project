"""
consider the passing a scaler to character to scaler up the power
make sure all KEY-VALUE PAIRS are useful
numbers to be changed
"""


def create_character() -> dict:
    """
    Create a beginning character containing user input.

    :postcondition:
    :return: character as a dictionary which contains user information
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
    :precondition: character must be a dictionary containing a key-value pair
    :postcondition:
    :return:
    """
    if character["current health"] > 0:
        return True
    else:
        return False


def accumulate_experience(character: dict):
    character["accumulated experience"] += 3


def check_if_leve_up(character: dict):
    if character["accumulated experience"] >= 10:
        character["level"] += 1
        character["current health"] = character["base health"] * character["level"]
        character["current damage"] = character["base damage"] * character["level"]
        character["accumulated experience"] -= 10
        print("Level up! Your health is fully recovered and you can now create higher damage.\n"
              "Your basic statistics is as follows:\n"
              f"Name: {character['name']}\n"
              f"Level: {character['level']}\n"
              f"HP: {character['current health']}\n"
              f"Damage: {character['current damage']}\n"
              f"Experience: {character['accumulated experience']}")


def reset_character_position(character: dict):
    character["current row"] = 0
    character["current column"] = 0
