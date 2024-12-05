from unittest import TestCase
from unittest.mock import patch
import io


from move import get_direction


class Test(TestCase):

    @patch("builtins.input", side_effect=["W"])
    def test_get_user_choice_when_player_wants_to_move_up(self, _):
        actual = get_direction()
        expected = "W"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["S"])
    def test_get_user_choice_when_player_wants_to_move_down(self, _):
        actual = get_direction()
        expected = "S"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["A"])
    def test_get_user_choice_when_player_wants_to_move_left(self, _):
        actual = get_direction()
        expected = "A"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["D"])
    def test_get_user_choice_when_player_wants_to_move_right(self, _):
        actual = get_direction()
        expected = "D"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["QUIT"])
    def test_get_user_choice_when_player_wants_to_quit(self, _):
        actual = get_direction()
        expected = "QUIT"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["w"])
    def test_get_user_choice_when_player_inputs_valid_direction_in_lower_case(self, _):
        actual = get_direction()
        expected = "W"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["123", "D"])
    def test_get_user_choice_when_player_inputs_invalid_then_valid_value(self, _, mock_stdout):
        actual_return = get_direction()
        expected_return = "D"
        expected_print = "Invalid input! Please try again.\n\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)
