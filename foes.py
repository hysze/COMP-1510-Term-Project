def create_enemy(scaler: int) -> dict:
    """
    Create enemies based on a scaler.

    :param scaler: an integer
    :precondition: scaler should be a non-zero positive integer practically
    :postcondition: create a dictionary containing two types of enemies, beast and dragon; each
                    enemy's statistics is calculated based on a scaler passed to this function,
                    where the scaler represents the round of game conducted
    :return: a dictionary

    >>> foes_one = create_enemy(1)
    >>> foes_one
    {'beast': {'health': 1, 'damage': 1}, 'dragon': {'health': 10, 'damage': 3}}
    >>> foes_two = create_enemy(3)
    >>> foes_two
    {'beast': {'health': 3, 'damage': 3}, 'dragon': {'health': 30, 'damage': 9}}
    """
    foes = {
        "beast": {
            "health": 1 * scaler,
            "damage": 1 * scaler
        },
        "dragon": {
            "health": 10 * scaler,
            "damage": 3 * scaler
        }
    }
    return foes


def boss_is_alive(game_map: dict):
    """
    Check whether the boss is still alive.

    :param game_map: a dictionary
    :precondition: game_map must be a well-constructed dictionary where the value "!" represents the
                   presence of the boss, i.e. the dragon, if it exists
    :postcondition: Return True when "!" as a string is a value inside the game_map dictionary and
                    False otherwise
    :return: a Boolean

    >>> game_map_one = {(0, 0): " ", (0, 1): "*", (0, 2): " ", \
                        (1, 0): "*", (1, 1): "!", (1, 2): " ", \
                        (2, 0): "*", (2, 1): " ", (2, 2): " "}
    >>> boss_is_alive(game_map_one)
    True
    >>> game_map_two = {(0, 0): " ", (0, 1): " ", (0, 2): " ", \
                        (1, 0): " ", (1, 1): " ", (1, 2): " ", \
                        (2, 0): " ", (2, 1): " ", (2, 2): " "}
    >>> boss_is_alive(game_map_two)
    False
    """
    if "!" in game_map.values():
        return True
    else:
        return False
