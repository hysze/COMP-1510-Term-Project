import character
import foes
import map
import move
import combat


def main():
    """
    Drive the program.
    """
    player = character.create_character()
    achieved_goal = False
    while player["current health"] > 0 and not achieved_goal:
        rows = 9
        columns = 9
        enemy = foes.create_enemy()
        board = map.create_map(rows, columns)
        achieved_goal = False
        while character.is_alive(player) and board[(int(rows / 2), int(columns / 2))] != " ":   # change it to is_alive as a boolean?
            map.print_map(rows, columns, board, player)
            direction = move.get_direction()
            if direction == "QUIT":
                achieved_goal = True
                break
            valid_move = move.validate_move(direction, player, board)
            if valid_move:
                move.move_character(direction, player)
                if combat.check_for_foes(player, board):
                    combat.beat_foe(player, enemy, board)   # change it to is_alive = combat.beat_foe(player, enemy, board)
                    map.clear_foe_on_map(player, board)
                    character.accumulate_experience(player)
                    character.check_if_leve_up(player)
            else:
                print("Warning! You're heading to a wrong way. Please enter a valid direction.")
        character.reset_character_position(player)
    if not character.is_alive(player):
        print("Game over! You are out of HP.")
    else:
        print("Congratulations! You found the ONLY WAY OUT!")


if __name__ == "__main__":
    main()
