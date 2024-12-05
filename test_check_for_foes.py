from unittest import TestCase
from unittest.mock import patch
import io

from combat import check_for_foes


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_when_there_is_a_beast(self, mock_stdout):
        character = {"current row": 1, "current column": 1}
        game_map = {(0, 0): " ", (0, 1): " ", (1, 0): "!", (1, 1): "*"}
        actual_return = check_for_foes(character, game_map)
        expected_return = True
        expected_print = "\nYou encounter a beast!\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_when_there_is_a_dragon(self, mock_stdout):
        character = {"current row": 1, "current column": 0}
        game_map = {(0, 0): " ", (0, 1): "*", (1, 0): "!", (1, 1): " "}
        actual_return = check_for_foes(character, game_map)
        expected_return = True
        expected_print = "\nYou encounter a dragon!\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    def test_check_for_foes_when_there_is_no_foe(self):
        character = {"current row": 0, "current column": 1}
        game_map = {(0, 0): " ", (0, 1): " ", (1, 0): "!", (1, 1): " "}
        actual = check_for_foes(character, game_map)
        expected = False
        self.assertEqual(actual, expected)
