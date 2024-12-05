def print_instructions(game_loop: int):
    """
    Print respective instructions based on the round of game.

    :param game_loop: an integer
    :precondition: game_loop must be a positive integer
    :postcondition: print respective statement according to the integer, representing the round of
                    game, passed to the function.

    >>> print_instructions(1) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    You wake up in the forest and are surrounded by aggressive beasts. A giant dragon is roaring
    to the moon at the center of the forest. You are forced to involve in endless combat.
    And there is only one way out!

    >>> print_instructions(2) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    You lose your consciousness after you beat the dragon. After a short while...
    Again, you wake up at starting point in the forest and are surrounded by aggressive beasts. The
    giant dragon is still alive, roaring at the center of the forest. This time, the dragon and
    beasts are fiercer than before. You are forced to involve in endless combat again.
    Remember, there is only one way out!
    """
    if game_loop == 1:
        print("\nYou wake up in the forest and are surrounded by aggressive beasts. A giant dragon "
              "is roaring to the moon at the center of the forest. You are forced to involve in "
              "endless combat.\n"
              "And there is only one way out!")

    elif game_loop == 2:
        print("\nYou lose your consciousness after you beat the dragon. After a short while...\n"
              "Again, you wake up at starting point in the forest and are surrounded by aggressive "
              "beasts. The giant dragon is still alive, roaring at the center of the forest. This "
              "time, the dragon and beasts are fiercer than before. You are forced to involve in "
              "endless combat again.\n"
              "Remember, there is only one way out!")

    else:
        print("\nYou hear someone murmuring \"not yet—\" and lose your consciousness again. "
              "After a short while...\n"
              "Again and again, you wake up at same place and are surrounded by beasts. The giant "
              "dragon is still alive. The dragon and beasts are on killing sprees. You are "
              "repeatedly forced to involve in endless combat once again, until you find the way "
              "out.\n"
              "REMEMBER, THERE IS ONLY ONE WAY OUT!")
