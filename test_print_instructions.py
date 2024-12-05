from unittest import TestCase
from unittest.mock import patch
import io


from narrative import print_instructions


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_first_round(self, mock_stdout):
        print_instructions(1)
        expected = ('\nYou wake up in the forest and are surrounded by beasts. A giant dragon is '
                    'at the center of the forest. You are forced to involve in endless combat.\n'
                    'And there is only one way out!\n')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_second_round(self, mock_stdout):
        print_instructions(2)
        expected = ("\nYou can't help falling asleep after you beat the dragon. After a short while"
                    "...\nAgain, you wake up at same place in the forest and are surrounded by "
                    "beasts. The giant dragon is still alive at the center of the forest. You are "
                    "forced to involve in endless combat again.\n"
                    "Remember, there is only one way out!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_third_round(self, mock_stdout):
        print_instructions(3)
        expected = ("\nYou can't help falling asleep after you beat the dragon. After a short while"
                    "...\nAgain and again, you wake up at same place are surrounded by beasts. The "
                    "giant dragon is still alive at the center of the forest. You are forced to "
                    "involve in endless combat once again.\n"
                    "REMEMBER, THERE IS ONLY ONE WAY OUT!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_after_third_round(self, mock_stdout):
        print_instructions(5)
        expected = ("\nYou can't help falling asleep after you beat the dragon. After a short while"
                    "...\nAgain and again, you wake up at same place are surrounded by beasts. The "
                    "giant dragon is still alive at the center of the forest. You are forced to "
                    "involve in endless combat once again.\n"
                    "REMEMBER, THERE IS ONLY ONE WAY OUT!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
