from unittest import TestCase
from unittest.mock import patch
import io

from move import validate_move
from map import create_map


class Test(TestCase):

    def test_validate_move_for_valid_move(self):
        character = {"current row": 1, "current column": 1}
        actual = validate_move("D", character, create_map(5, 5))
        expected = True
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_for_invalid_move_across_minimum_column(self, mock_stdout):
        character = {"current row": 0, "current column": 0}
        actual_return = validate_move("A", character, create_map(5, 5))
        expected_return = False
        expected_print = ("\nWarning! You're heading to a wrong way. Please enter a valid "
                          "direction.\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_for_invalid_move_across_maximum_column(self, mock_stdout):
        character = {"current row": 0, "current column": 4}
        actual_return = validate_move("D", character, create_map(5, 5))
        expected_return = False
        expected_print = ("\nWarning! You're heading to a wrong way. Please enter a valid "
                          "direction.\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_for_invalid_move_across_minimum_row(self, mock_stdout):
        character = {"current row": 0, "current column": 4}
        actual_return = validate_move("W", character, create_map(5, 5))
        expected_return = False
        expected_print = ("\nWarning! You're heading to a wrong way. Please enter a valid "
                          "direction.\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_for_invalid_move_across_maximum_row(self, mock_stdout):
        character = {"current row": 4, "current column": 0}
        actual_return = validate_move("S", character, create_map(5, 5))
        expected_return = False
        expected_print = ("\nWarning! You're heading to a wrong way. Please enter a valid "
                          "direction.\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)
