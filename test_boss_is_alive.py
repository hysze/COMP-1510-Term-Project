from unittest import TestCase


from foes import boss_is_alive


class Test(TestCase):

    def test_boss_is_alive_when_boss_is_still_on_the_map(self):
        game_map = {(0, 0): " ", (0, 1): "*", (0, 2): " ",
                    (1, 0): "*", (1, 1): "!", (1, 2): " ",
                    (2, 0): "*", (2, 1): " ", (2, 2): " "}
        actual = boss_is_alive(game_map)
        expected = True
        self.assertEqual(actual, expected)

    def test_boss_is_alive_when_boss_is_no_longer_on_the_map(self):
        game_map = {(0, 0): " ", (0, 1): " ", (0, 2): " ",
                    (1, 0): " ", (1, 1): " ", (1, 2): " ",
                    (2, 0): " ", (2, 1): " ", (2, 2): " "}
        actual = boss_is_alive(game_map)
        expected = False
        self.assertEqual(actual, expected)
