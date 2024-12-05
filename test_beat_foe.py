from unittest import TestCase
from unittest.mock import patch


from combat import beat_foe


class Test(TestCase):

    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', side_effect=[1])
    def test_beat_foe_when_the_player_beats_the_foe(self, _, __):
        player = {"current health": 1, "current damage": 1, "current row": 1, "current column": 1}
        foes = {'beast': {'health': 1, 'damage': 1}, 'dragon': {'health': 10, 'damage': 3}}
        board = {(1, 1): "*"}
        actual = beat_foe(player, foes, board)
        expected = True
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', side_effect=[1])
    def test_beat_foe_when_the_foe_beats_the_player(self, _, __):
        player = {"current health": 1, "current damage": 3, "current row": 3, "current column": 3}
        foes = {'beast': {'health': 1, 'damage': 1}, 'dragon': {'health': 10, 'damage': 3}}
        board = {(3, 3): "!"}
        actual = beat_foe(player, foes, board)
        expected = False
        self.assertEqual(actual, expected)
