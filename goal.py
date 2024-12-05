def achieve_goal(direction: str) -> bool:
    """
    Check whether the player achieves the goal.

    :param direction: a string
    :postcondition: return True if direction is "QUIT" and otherwise False
    :return: a Boolean

    >>> achieve_goal("QUIT")
    True
    >>> achieve_goal("W")
    False
    """
    if direction == "QUIT":
        return True
    else:
        return False
