from unittest import TestCase


from foes import create_enemy


class Test(TestCase):
    def test_create_enemy_with_a_small_positive_number(self):
        actual = create_enemy(1)
        expected = {"beast": {"health": 1, "damage": 1}, "dragon": {"health": 10, "damage": 3}}
        self.assertEqual(actual, expected)

    def test_create_enemy_with_a_medium_positive_number(self):
        actual = create_enemy(5)
        expected = {"beast": {"health": 5, "damage": 5}, "dragon": {"health": 50, "damage": 15}}
        self.assertEqual(actual, expected)

    def test_create_enemy_with_a_large_positive_number(self):
        actual = create_enemy(10)
        expected = {"beast": {"health": 10, "damage": 10}, "dragon": {"health": 100, "damage": 30}}
        self.assertEqual(actual, expected)
