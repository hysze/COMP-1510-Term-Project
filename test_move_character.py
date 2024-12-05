from unittest import TestCase


from move import move_character


class Test(TestCase):

    def test_move_character_upwards(self):
        actual = {"current row": 2, "current column": 2}
        move_character("W", actual)
        expected = {"current row": 1, "current column": 2}
        self.assertEqual(actual, expected)

    def test_move_character_downwards(self):
        actual = {"current row": 3, "current column": 3}
        move_character("S", actual)
        expected = {"current row": 4, "current column": 3}
        self.assertEqual(actual, expected)

    def test_move_character_leftwards(self):
        actual = {"current row": 1, "current column": 1}
        move_character("A", actual)
        expected = {"current row": 1, "current column": 0}
        self.assertEqual(actual, expected)

    def test_move_character_rightwards(self):
        actual = {"current row": 2, "current column": 2}
        move_character("D", actual)
        expected = {"current row": 2, "current column": 3}
        self.assertEqual(actual, expected)
