from unittest import TestCase
from unittest.mock import patch
import io


from character import create_character


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Descartes"])
    def test_create_character_when_user_input_is_all_english_characters(self, _, mock_stdout):
        actual_return = create_character()
        expected_return = {"name": "Descartes", "level": 1, "current health": 10,
                           "current damage": 1, "base health": 10, "base damage": 1,
                           "accumulated experience": 0, "current row": 0, "current column": 0}
        expected_print = ("\nWelcome again, Descartes! Your basic statistics is as follows:\n"
                          "Name: Descartes\n"
                          "Level: 1\n"
                          "HP: 10\n"
                          "Damage: 1\n"
                          "Experience: 0\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["123!@#"])
    def test_create_character_when_user_input_is_non_english_characters(self, _, mock_stdout):
        actual_return = create_character()
        expected_return = {"name": "123!@#", "level": 1, "current health": 10,
                           "current damage": 1, "base health": 10, "base damage": 1,
                           "accumulated experience": 0, "current row": 0, "current column": 0}
        expected_print = ("\nWelcome again, 123!@#! Your basic statistics is as follows:\n"
                          "Name: 123!@#\n"
                          "Level: 1\n"
                          "HP: 10\n"
                          "Damage: 1\n"
                          "Experience: 0\n")
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_name(self, _):
        result = create_character()
        self.assertIn("name", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_level(self, _):
        result = create_character()
        self.assertIn("level", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_current_health(self, _):
        result = create_character()
        self.assertIn("current health", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_current_damage(self, _):
        result = create_character()
        self.assertIn("current damage", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_base_health(self, _):
        result = create_character()
        self.assertIn("base health", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_base_damage(self, _):
        result = create_character()
        self.assertIn("base damage", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_accumulated_experience(self, _):
        result = create_character()
        self.assertIn("accumulated experience", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_current_row(self, _):
        result = create_character()
        self.assertIn("current row", result)

    @patch('builtins.input', side_effect=["testing"])
    def test_create_character_contains_current_column(self, _):
        result = create_character()
        self.assertIn("current column", result)
