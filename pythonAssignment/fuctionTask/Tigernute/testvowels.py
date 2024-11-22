from unittest import TestCase
import vowels

class TestCountVowelsFunction(TestCase):
    def test_that_count_vowels_function_exists(self):
        string = ["python is sweet"]
        vowels.count_vowels(string)

    def test_that_count_vowels_function_returns_correct_value(self):
        string = ["python is sweet"]
        actual = vowels.count_vowels(string)
        expected = 4
        self.assertEqual(actual, expected)


