from unittest import TestCase
from unittest.mock import patch


from map import create_map


class Test(TestCase):

    @patch('random.randint', side_effect=[0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 0, 3, 1, 3, 2, 3, 3,
                                          3, 4, 3])
    def test_create_map_with_no_duplicate_pair_of_random_coordinates(self, _):
        actual = create_map(5, 5)
        expected = {(0, 0): " ", (0, 1): "*", (0, 2): " ", (0, 3): "*", (0, 4): " ",
                    (1, 0): " ", (1, 1): "*", (1, 2): " ", (1, 3): "*", (1, 4): " ",
                    (2, 0): " ", (2, 1): "*", (2, 2): "!", (2, 3): "*", (2, 4): " ",
                    (3, 0): " ", (3, 1): "*", (3, 2): " ", (3, 3): "*", (3, 4): " ",
                    (4, 0): " ", (4, 1): "*", (4, 2): " ", (4, 3): "*", (4, 4): " "}
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 0, 3, 1, 3, 2,
                                          3, 3, 3, 4, 3])
    def test_create_map_with_duplicate_pair_of_random_coordinates(self, _):
        actual = create_map(5, 5)
        expected = {(0, 0): " ", (0, 1): "*", (0, 2): " ", (0, 3): "*", (0, 4): " ",
                    (1, 0): " ", (1, 1): "*", (1, 2): " ", (1, 3): "*", (1, 4): " ",
                    (2, 0): " ", (2, 1): "*", (2, 2): "!", (2, 3): "*", (2, 4): " ",
                    (3, 0): " ", (3, 1): "*", (3, 2): " ", (3, 3): "*", (3, 4): " ",
                    (4, 0): " ", (4, 1): "*", (4, 2): " ", (4, 3): "*", (4, 4): " "}
        self.assertEqual(actual, expected)
