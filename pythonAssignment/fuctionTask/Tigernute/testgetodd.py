from unittest import TestCase
import getodd

class TestgetOddFunction(TestCase):
    def test_that_get_odd_function_exists(self):
        numbers = [1,2,3,4,5]
        getodd.get_odd(numbers)
    def test_that_get_odd_function_returns_correct_value(self):
        numbers = [1,2,3,4,5]
        actual = getodd.get_odd(numbers)
        expected = 9
        self.assertEqual(actual, expected)

