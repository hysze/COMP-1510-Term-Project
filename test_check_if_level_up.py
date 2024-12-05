from unittest import TestCase
from unittest.mock import patch
import io


from character import check_if_level_up


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_level_up_when_character_have_enough_experience_to_level_up(self, mock_stdout):
        actual = {"name": "Aristotle", "level": 1, "current health": 1, "current damage": 1,
                  "base health": 10, "base damage": 1, "accumulated experience": 15}
        check_if_level_up(actual)
        expected = {"name": "Aristotle", "level": 2, "current health": 20, "current damage": 2,
                    "base health": 10, "base damage": 1, "accumulated experience": 5}
        expected_print = ("\nLevel up! Your health is fully recovered, and you can now create "
                          "higher damage.\n"
                          "Your basic statistics is as follows:\n"
                          "Name: Aristotle\n"
                          "Level: 2\n"
                          "HP: 20\n"
                          "Damage: 2\n"
                          "Experience: 5\n")
        self.assertEqual(actual, expected)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    def test_check_if_level_up_when_character_does_not_have_enough_experience(self):
        actual = {"name": "Descartes", "level": 1, "current health": 10, "current damage": 1,
                  "base health": 10, "base damage": 1, "accumulated experience": 0}
        check_if_level_up(actual)
        expected = {"name": "Descartes", "level": 1, "current health": 10, "current damage": 1,
                    "base health": 10, "base damage": 1, "accumulated experience": 0}
        self.assertEqual(actual, expected)
