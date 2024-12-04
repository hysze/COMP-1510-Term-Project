def print_instructions(game_loop: int):
    """
    Print respective instructions based on the round of game.

    :param game_loop: an integer
    :precondition: game_loop must be a positive integer
    :postcondition: print respective statement according to the integer, representing the round of
                    game, passed to the function.

    >>> print_instructions(1)
    <BLANKLINE>
    You wake up in the forest and are surrounded by beasts. A giant dragon is at the center of the forest. You are forced to involve in endless combat.
    And there is only one way out!

    >>> print_instructions(2)
    <BLANKLINE>
    You can't help falling asleep after you beat the dragon. After a short while...
    Again, you wake up at same place in the forest and are surrounded by beasts. The giant dragon is still alive at the center of the forest. You are forced to involve in endless combat again.
    Remember, there is only one way out!
    """
    if game_loop == 1:
        print("\nYou wake up in the forest and are surrounded by beasts. A giant dragon is at the "
              "center of the forest. You are forced to involve in endless combat.\n"
              "And there is only one way out!")

    elif game_loop == 2:
        print("\nYou can't help falling asleep after you beat the dragon. After a short while...\n"
              "Again, you wake up at same place in the forest and are surrounded by beasts. The "
              "giant dragon is still alive at the center of the forest. You are forced to involve "
              "in endless combat again.\n"
              "Remember, there is only one way out!")

    else:
        print("\nYou can't help falling asleep after you beat the dragon. After a short while...\n"
              "Again and again, you wake up at same place are surrounded by beasts. The giant "
              "dragon is still alive at the center of the forest. You are forced to involve in "
              "endless combat once again.\n"
              "REMEMBER, THERE IS ONLY ONE WAY OUT!")
