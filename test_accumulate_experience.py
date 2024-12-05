from unittest import TestCase


from character import accumulate_experience


class Test(TestCase):

    def test_accumulate_experience_when_initial_experience_is_zero(self):
        actual = {"accumulated experience": 0}
        accumulate_experience(actual)
        expected = {"accumulated experience": 3}
        self.assertEqual(actual, expected)

    def test_accumulate_experience_when_initial_experience_is_a_small_integer(self):
        actual = {"accumulated experience": 2}
        accumulate_experience(actual)
        expected = {"accumulated experience": 5}
        self.assertEqual(actual, expected)

    def test_accumulate_experience_when_initial_experience_is_a_medium_integer(self):
        actual = {"accumulated experience": 5}
        accumulate_experience(actual)
        expected = {"accumulated experience": 8}
        self.assertEqual(actual, expected)

    def test_accumulate_experience_when_initial_experience_is_a_large_integer(self):
        actual = {"accumulated experience": 8}
        accumulate_experience(actual)
        expected = {"accumulated experience": 11}
        self.assertEqual(actual, expected)
