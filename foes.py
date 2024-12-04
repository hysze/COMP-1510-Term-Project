"""
make sure ALL KEYS are useful
numbers to be changed
"""


def create_enemy(scaler: int) -> dict:
    """
    scaler is round
    :param scaler:
    :return:
    """
    foes = {
        "beast": {
            "name": "beast",
            "health": 1 * scaler,
            "damage": 1 * scaler
        },
        "dragon": {
            "name": "dragon",
            "health": 1 * scaler,
            "damage": 3 * scaler
        }
    }
    return foes


def boss_is_alive(game_map: dict):
    if "!" in game_map.values():
        return True
    else:
        return False
