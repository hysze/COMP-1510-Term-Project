import character
import foes
import map
import move
import combat
import narrative
import goal


def main():
    """
    Drive the program.
    """
    player = character.create_character()
    goal_obtained = False
    game_loop = 1
    while player["current health"] > 0 and not goal_obtained:
        narrative.print_instructions(game_loop)
        rows = 9
        columns = 9
        enemy = foes.create_enemy(game_loop)
        board = map.create_map(rows, columns)
        while character.is_alive(player) and foes.boss_is_alive(board):
            map.print_map(rows, columns, board, player)
            direction = move.get_direction()
            goal_obtained = goal.achieve_goal(direction)
            if goal_obtained:
                break
            else:
                valid_move = move.validate_move(direction, player, board)
                if valid_move:
                    move.move_character(direction, player)
                    if combat.check_for_foes(player, board):
                        combat.beat_foe(player, enemy, board)
                        map.clear_foe_on_map(player, board)
                        character.accumulate_experience(player)
                        character.check_if_level_up(player)
        character.reset_character_position(player)
        game_loop += 1
    if not character.is_alive(player):
        print("\nGame over! You die in the forest running out of HP. Your soul will be staying "
              "here forever...")
    else:
        print("\nCongratulations! You find the ONLY WAY OUT and can come back to BCIT to continue "
              "your endless work! :)")


if __name__ == "__main__":
    main()
