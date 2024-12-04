import random


def check_for_foes(character: dict, board: dict) -> bool:
    """
    Check if there is a foe at the player's current location.

    :param character: a dictionary
    :param board: a dictionary
    :precondition: character must be a dictionary containing two keys "current row" and "current
                   column"; board must be a dictionary containing tuples as keys, and each tuple
                   contains two integers representing row and column in order
    :postcondition: return True when the value corresponded to the character's current location
                    inside the board dictionary is not a space character, which means there is a
                    foe; return False when the corresponding value is a space character, meaning
                    that there is nothing
    :return: a Boolean where True represents there is a foe and False represents there is not

    >>> player_one = {"current row": 1, "current column": 1}
    >>> board_one = {(0, 0): " ", (0, 1): " ", (1, 0): "!", (1, 1): "*"}
    >>> check_for_foes(player_one, board_one)
    True
    >>> player_two = {"current row": 0, "current column": 0}
    >>> board_two = {(0, 0): " "}
    >>> check_for_foes(player_two, board_two)
    False
    """
    location = (character["current row"], character["current column"])
    if board[location] != " ":
        return True
    else:
        return False


def beat_foe(character: dict, foes: dict, board: dict) -> bool:
    """
    Check whether the player beat the foe they encounter.

    :param character: a dictionary
    :param foes: a dictionary
    :param board: a dictionary
    :precondition: character must be a well-structured dictionary containing the three keys "current
                   row", "current column" and "current health" where each corresponds to a numeric
                   value; foes must be a dictionary containing the key "beast" and "dragon" and each
                   corresponds to another sub-dictionary; board must be a dictionary containing
                   tuples where each tuple contains two integers representing row and column
    :postcondition: Call battle_with_foe function to fight with a foe; return True if the numeric
                    value corresponded to the character's "current health" is larger than zero and
                    return False if less than or equal to zero
    :return: a Boolean where True represents the player beat foe and otherwises False
    """
    location = (character["current row"], character["current column"])

    if board[location] == "*":
        print("You encounter a beast!")
        enemy = {"health": foes["beast"]["health"], "damage": foes["beast"]["damage"]}
    else:
        print("You encounter a dragon!")
        enemy = {"health": foes["dragon"]["health"], "damage": foes["dragon"]["damage"]}

    battle_with_foe(character, enemy)

    if character["current health"] > 0:
        return True
    else:
        return False


def battle_with_foe(character: dict, foe: dict):
    """
    Play a number-guessing game to battle with a foe.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character must be a dictionary containing the two keys "current health" and
                   "current damage"; foe must be a dictionary containing the two keys "health" and
                    "damage"
    :postcondition: Generate a random number for the player to guess. Correct guesses will deduct
                    the foe's health by the character's damage while wrong guesses will deduct the
                    character's health by the foe's damage; this function ends until either side's
                    health is below or equal to zero
    """
    while character["current health"] > 0 and foe["health"] > 0:
        random_number = random.randint(1, 3)
        user_guess = input("Guess an integer between 1 and 3 inclusive: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            character["current health"] -= foe["damage"]
            print(f"Invalid input! You miss you turn, and get hit by your foe.\n"
                  f"Your remaining HP is {character['current health']}.\n")
        else:
            if user_guess == random_number:
                foe["health"] -= character["current damage"]
                print(f"Correct! You create {character['current damage']} damage to your foe.\n"
                      f"Your foe's remaining HP is {foe['health']}.\n")
            else:
                character["current health"] -= foe["damage"]
                print(f"Wrong guess! Your foe create {foe["damage"]} damage to you.\n"
                      f"Your current health is {character['current health']}.\n")
