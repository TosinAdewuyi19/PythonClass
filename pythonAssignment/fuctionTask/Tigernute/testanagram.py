from unittest import TestCase
import anagram

class TestAnagramFunction(TestCase):
    def test_that_sort_anagram_function_exists(self):
        str_one = ("listen")
        str_two = ("silent")
        anagram.sort_anagram(str_one, str_two)

    def test_that_sort_anagram_function_returns_correct_value(self):
        str_one = ("listen")
        str_two = ("silent")
        actual = anagram.sort_anagram(str_one, str_two)
        expected = True
        self.assertEqual(actual, expected)
