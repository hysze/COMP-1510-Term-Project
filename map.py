import random


def create_map(rows: int, columns: int) -> dict:
    game_map = {}
    for row in range(rows):
        for column in range(columns):
            game_map[(row, column)] = " "

    center_point = (int(rows / 2), int(columns / 2))
    game_map[center_point] = "!"

    foe_count = 0
    while foe_count < rows + columns:
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        random_point = (random_row, random_column)
        if random_point != (0, 0) and game_map[random_point] == " ":
            game_map[random_point] = "*"
            foe_count += 1

    return game_map


def print_map(rows: int, columns: int, game_map: dict, character: dict):
    character_current_location = (character["current row"], character["current column"])
    print()
    for row in range(rows):
        for column in range(columns):
            if (row, column) != character_current_location:
                print(f"[{game_map[(row, column)]}]", end='')
            else:
                print("[@]", end='')
        print()
    print("[@] - You; [*] - Beast; [!] - Dragon")


def clear_foe_on_map(character: dict, game_map: dict):
    character_current_location = (character["current row"], character["current column"])
    game_map[character_current_location] = " "
