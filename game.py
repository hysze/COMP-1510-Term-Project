import character
import foes
import map
import move
import combat
import narrative


def main():
    """
    Drive the program.
    """
    player = character.create_character()
    achieved_goal = False
    game_loop = 1
    while player["current health"] > 0 and not achieved_goal:
        narrative.print_instructions(game_loop)
        rows = 9
        columns = 9
        enemy = foes.create_enemy(game_loop)
        board = map.create_map(rows, columns)
        while character.is_alive(player) and foes.boss_is_alive(board):
            map.print_map(rows, columns, board, player)
            direction = move.get_direction()
            if direction == "QUIT":
                achieved_goal = True
                break
            valid_move = move.validate_move(direction, player, board)
            if valid_move:
                move.move_character(direction, player)
                if combat.check_for_foes(player, board):
                    combat.beat_foe(player, enemy, board)
                    map.clear_foe_on_map(player, board)
                    character.accumulate_experience(player)
                    character.check_if_level_up(player)
            # else:
            #     print("Warning! You're heading to a wrong way. Please enter a valid direction.")
        character.reset_character_position(player)
        game_loop += 1
    if not character.is_alive(player):
        print("\nGame over! You are out of HP.")
    else:
        print("\nCongratulations! You find the ONLY WAY OUT!")


if __name__ == "__main__":
    main()
