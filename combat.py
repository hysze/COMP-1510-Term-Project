import random


def check_for_foes(player: dict, board: dict) -> bool:
    location = (player["current row"], player["current column"])
    if board[location] != " ":
        return True
    else:
        return False


def beat_foe(player: dict, foes: dict, board: dict) -> bool:
    location = (player["current row"], player["current column"])
    if board[location] == "*":
        print("You encounter a beast!")
        beast = {"health": foes["beast"]["health"], "damage": foes["beast"]["damage"]}
        battle_with_foe(player, beast)
    else:
        print("You encounter a dragon!")
        dragon = {"health": foes["dragon"]["health"], "damage": foes["dragon"]["damage"]}
        battle_with_foe(player, dragon)

    if player["current health"] > 0:
        return True
    else:
        return False


def battle_with_foe(player, foe):
    while player["current health"] > 0 and foe["health"] > 0:
        random_number = random.randint(1, 3)
        user_guess = input("Guess an integer between 1 and 3 inclusive: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            player["current health"] -= foe["damage"]
            print(f"Invalid input! You miss you turn, and get hit by your foe.\n"
                  f"Your remaining HP is {player['current health']}.")
        else:
            if user_guess == random_number:
                foe["health"] -= player["current damage"]
                print(f"Correct guess! You create {player['current damage']} damage to your foe.\n"
                      f"Your foe's remaining HP is {foe['health']}.")
            else:
                player["current health"] -= foe["damage"]
                print(f"Wrong guess! Your foe create {foe["damage"]} damage to you.\n"
                      f"Your current health is {player['current health']}.")
