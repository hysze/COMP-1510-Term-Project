"""
make sure ALL KEYS are useful
numbers to be changed
"""


def create_enemy() -> dict:
    foes = {
        "beast": {
            "name": "beast",
            "health": 1,
            "damage": 1
        },
        "dragon": {
            "name": "dragon",
            "health": 10,
            "damage": 3
        }
    }
    return foes
