from unittest import TestCase


from map import clear_foe_on_map


class Test(TestCase):

    def test_clear_foe_on_map_when_characters_current_position_has_nothing(self):
        character = {"current row": 0, "current column": 0}
        game_map = {(0, 0): " ", (0, 1): "*", (0, 2): "*", (1, 0): "*", (1, 1): "!", (1, 2): " ",
                    (2, 0): "*", (2, 1): "*", (2, 2): "*"}
        clear_foe_on_map(character, game_map)
        actual = game_map[(character["current row"], character["current column"])]
        expected = " "
        self.assertEqual(actual, expected)

    def test_clear_foe_on_map_when_characters_current_position_has_a_foe(self):
        character = {"current row": 2, "current column": 1}
        game_map = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (1, 0): "*", (1, 1): "!", (1, 2): " ",
                    (2, 0): " ", (2, 1): "*", (2, 2): "*"}
        clear_foe_on_map(character, game_map)
        actual = game_map[(character["current row"], character["current column"])]
        expected = " "
        self.assertEqual(actual, expected)
