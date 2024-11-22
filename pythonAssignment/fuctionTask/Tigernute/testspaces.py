from unittest import TestCase
import spaces

class TestRemovSpacesFunction(TestCase):
    def test_that_remove_spaces_function_exists(self):
        string = ["hello world"]
        spaces.remove_spaces(string)

    def test_that_remove_spaces_function_returns_correct_value(self):
        string = ["hello world"]
        actual = spaces.remove_spaces (string)
        expected = ["helloworld"]
        self.assertEqual(actual, expected)


