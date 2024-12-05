from unittest import TestCase


from character import is_alive


class Test(TestCase):

    def test_is_alive_when_character_hp_is_non_zero_positive_integer(self):
        character = {"current health": 5}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_when_character_hp_is_zero(self):
        character = {"current health": 0}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_when_character_hp_is_non_zero_negative_integer(self):
        character = {"current health": -1}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)
