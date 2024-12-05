from unittest import TestCase


from character import reset_character_position


class Test(TestCase):

    def test_reset_character_position(self):
        actual = {"current row": 4, "current column": 4}
        reset_character_position(actual)
        expected = {"current row": 0, "current column": 0}
        self.assertEqual(actual, expected)
