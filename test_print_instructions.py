from unittest import TestCase
from unittest.mock import patch
import io


from narrative import print_instructions


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_first_round(self, mock_stdout):
        print_instructions(1)
        expected = ("\nYou wake up in the forest and are surrounded by aggressive beasts. A giant "
                    "dragon is roaring to the moon at the center of the forest. You are forced to "
                    "involve in endless combat.\n"
                    "And there is only one way out!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_second_round(self, mock_stdout):
        print_instructions(2)
        expected = ("\nYou lose your consciousness after you beat the dragon. After a short "
                    "while...\n"
                    "Again, you wake up at starting point in the forest and are surrounded by "
                    "aggressive beasts. The giant dragon is still alive, roaring at the center of "
                    "the forest. This time, the dragon and beasts are fiercer than before. You are "
                    "forced to involve in endless combat again.\n"
                    "Remember, there is only one way out!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_third_round(self, mock_stdout):
        print_instructions(3)
        expected = ("\nYou hear someone murmuring \"not yet—\" and lose your consciousness again. "
                    "After a short while...\n"
                    "Again and again, you wake up at same place and are surrounded by beasts. The "
                    "giant dragon is still alive. The dragon and beasts are on killing sprees. You "
                    "are repeatedly forced to involve in endless combat once again, until you find "
                    "the way out.\n"
                    "REMEMBER, THERE IS ONLY ONE WAY OUT!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_when_it_is_after_third_round(self, mock_stdout):
        print_instructions(5)
        expected = ("\nYou hear someone murmuring \"not yet—\" and lose your consciousness again. "
                    "After a short while...\n"
                    "Again and again, you wake up at same place and are surrounded by beasts. The "
                    "giant dragon is still alive. The dragon and beasts are on killing sprees. You "
                    "are repeatedly forced to involve in endless combat once again, until you find "
                    "the way out.\n"
                    "REMEMBER, THERE IS ONLY ONE WAY OUT!\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
