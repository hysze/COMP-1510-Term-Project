from unittest import TestCase
from unittest.mock import patch
import io


from map import print_map


class Test(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_for_small_sized_map(self, mock_stdout):
        game_map = {(0, 0): " ", (0, 1): "*", (0, 2): "*", (1, 0): "*", (1, 1): "!", (1, 2): " ",
                    (2, 0): "*", (2, 1): "*", (2, 2): "*"}
        character = {"current row": 0, "current column": 0}
        print_map(3, 3, game_map, character)
        expected = ("\n[@] - You; [*] - Beast; [!] - Dragon\n\n"
                    "[@][*][*]\n"
                    "[*][!][ ]\n"
                    "[*][*][*]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_for_medium_sized_map(self, mock_stdout):
        game_map = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (0, 3): " ", (0, 4): " ",
                    (1, 0): " ", (1, 1): " ", (1, 2): " ", (1, 3): "*", (1, 4): " ",
                    (2, 0): "*", (2, 1): "*", (2, 2): "!", (2, 3): " ", (2, 4): " ",
                    (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): "*", (3, 4): " ",
                    (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " "}
        character = {"current row": 1, "current column": 2}
        print_map(5, 5, game_map, character)
        expected = ("\n[@] - You; [*] - Beast; [!] - Dragon\n\n"
                    "[ ][ ][ ][ ][ ]\n"
                    "[ ][ ][@][*][ ]\n"
                    "[*][*][!][ ][ ]\n"
                    "[ ][ ][ ][*][ ]\n"
                    "[ ][ ][ ][ ][ ]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_for_large_sized_map(self, mock_stdout):
        game_map = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (0, 3): " ", (0, 4): "*",
                    (0, 5): " ", (0, 6): " ", (0, 7): " ", (0, 8): " ",
                    (1, 0): " ", (1, 1): " ", (1, 2): " ", (1, 3): " ", (1, 4): "*",
                    (1, 5): " ", (1, 6): " ", (1, 7): " ", (1, 8): " ",
                    (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ",
                    (2, 5): "*", (2, 6): " ", (2, 7): " ", (2, 8): " ",
                    (3, 0): "*", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ",
                    (3, 5): " ", (3, 6): " ", (3, 7): " ", (3, 8): " ",
                    (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): "!",
                    (4, 5): " ", (4, 6): " ", (4, 7): " ", (4, 8): " ",
                    (5, 0): " ", (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ",
                    (5, 5): " ", (5, 6): " ", (5, 7): " ", (5, 8): " ",
                    (6, 0): " ", (6, 1): " ", (6, 2): " ", (6, 3): " ", (6, 4): " ",
                    (6, 5): " ", (6, 6): " ", (6, 7): " ", (6, 8): " ",
                    (7, 0): " ", (7, 1): " ", (7, 2): " ", (7, 3): " ", (7, 4): " ",
                    (7, 5): " ", (7, 6): " ", (7, 7): " ", (7, 8): " ",
                    (8, 0): " ", (8, 1): " ", (8, 2): " ", (8, 3): " ", (8, 4): " ",
                    (8, 5): " ", (8, 6): "*", (8, 7): "*", (8, 8): "*", }
        character = {"current row": 0, "current column": 3}
        print_map(9, 9, game_map, character)
        expected = ("\n[@] - You; [*] - Beast; [!] - Dragon\n\n"
                    "[ ][ ][ ][@][*][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][*][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][ ][*][ ][ ][ ]\n"
                    "[*][ ][ ][ ][ ][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][!][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][ ][ ][ ][ ][ ]\n"
                    "[ ][ ][ ][ ][ ][ ][*][*][*]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
