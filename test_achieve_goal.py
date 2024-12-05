from unittest import TestCase


from goal import achieve_goal


class Test(TestCase):

    def test_achieve_goal_when_the_player_achieves_goals(self):
        actual = achieve_goal("QUIT")
        expected = True
        self.assertEqual(actual, expected)

    def test_achieve_goal_when_the_player_does_not_achieve_goals(self):
        actual = achieve_goal("S")
        expected = False
        self.assertEqual(actual, expected)
