from unittest import TestCase
from unittest.mock import patch
import io


from combat import battle_with_foe


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', side_effect=[1])
    def test_battle_with_foe_when_player_beats_foe_in_one_hit(self, _, __, mock_stdout):
        character = {"current health": 10, "current damage": 1}
        foe = {"health": 1, "damage": 1}
        battle_with_foe(character, foe)
        actual_foe_health = foe["health"]
        expected_foe_health = 0
        expected_print = ("\nCorrect! You create 1 damage to your foe.\n"
                          "Your foe's remaining HP is 0.\n")
        self.assertEqual(actual_foe_health, expected_foe_health)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1, 2])
    @patch('random.randint', side_effect=[1, 2])
    def test_battle_with_foe_when_player_beats_foe_in_multiple_hits(self, _, __, mock_stdout):
        character = {"current health": 10, "current damage": 2}
        foe = {"health": 3, "damage": 3}
        battle_with_foe(character, foe)
        actual_foe_health = foe["health"]
        expected_foe_health = -1
        expected_print = ("\nCorrect! You create 2 damage to your foe.\n"
                          "Your foe's remaining HP is 1.\n"
                          "\nCorrect! You create 2 damage to your foe.\n"
                          "Your foe's remaining HP is -1.\n")
        self.assertEqual(actual_foe_health, expected_foe_health)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[3])
    @patch('random.randint', side_effect=[1])
    def test_battle_with_foe_when_foe_beats_character_in_one_hit(self, _, __, mock_stdout):
        character = {"current health": 1, "current damage": 1}
        foe = {"health": 1, "damage": 1}
        battle_with_foe(character, foe)
        actual_character_health = character["current health"]
        expected_character_health = 0
        expected_print = ("\nWrong guess! You miss your attack. Your foe creates 1 damage to you.\n"
                          "Your current health is 0.\n")
        self.assertEqual(actual_character_health, expected_character_health)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[3, 1])
    @patch('random.randint', side_effect=[1, 2])
    def test_battle_with_foe_when_foe_beats_character_in_multiple_hit(self, _, __, mock_stdout):
        character = {"current health": 5, "current damage": 1}
        foe = {"health": 3, "damage": 3}
        battle_with_foe(character, foe)
        actual_character_health = character["current health"]
        expected_character_health = -1
        expected_print = ("\nWrong guess! You miss your attack. Your foe creates 3 damage to you.\n"
                          "Your current health is 2.\n"
                          "\nWrong guess! You miss your attack. Your foe creates 3 damage to you.\n"
                          "Your current health is -1.\n")
        self.assertEqual(actual_character_health, expected_character_health)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["A"])
    @patch('random.randint', side_effect=[1])
    def test_battle_with_foe_when_player_inputs_invalid_input(self, _, __, mock_stdout):
        character = {"current health": 1, "current damage": 1}
        foe = {"health": 1, "damage": 1}
        battle_with_foe(character, foe)
        actual_character_health = character["current health"]
        expected_character_health = 0
        expected_print = ("\nInvalid input! You miss you turn, and get hit by your foe.\n"
                          "Your remaining HP is 0.\n")
        self.assertEqual(actual_character_health, expected_character_health)
        self.assertEqual(mock_stdout.getvalue(), expected_print)
