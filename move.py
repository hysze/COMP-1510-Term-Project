def get_direction() -> str:
    direction = input("Enter \"W-A-S-D\" to move up-left-down-right or \"Quit\" to quit the game: ")
    direction = direction.upper()
    valid_input = ["W", "A", "S", "D", "QUIT"]
    if direction not in valid_input:
        print("Invalid input! Please try again.")
        direction = get_direction()
    return direction


def validate_move(direction: str, character: dict, game_map: dict) -> bool:
    destination_row = character["current row"]
    destination_column = character["current column"]
    if direction == "W":
        destination_row -= 1
    if direction == "S":
        destination_row += 1
    if direction == "A":
        destination_column -= 1
    if direction == "D":
        destination_column += 1
    if (destination_row, destination_column) in game_map:
        return True
    else:
        return False


def move_character(direction: str, character: dict):
    if direction == "W":
        character["current row"] -= 1
    if direction == "S":
        character["current row"] += 1
    if direction == "A":
        character["current column"] -= 1
    if direction == "D":
        character["current column"] += 1
