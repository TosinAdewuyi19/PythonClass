from unittest import TestCase
import reversed

class TestGetReversedFunction(TestCase):
    def test_that_get_reversed_function_exists(self):
        string = ["hello"]
        reversed.get_reversed(string)

    def test_that_get_reversed_function_returns_correct_value(self):
        string = ["hello"]
        actual = reversed.get_reversed (string)
        expected = ["olleh"]
        self.assertEqual(actual, expected)

