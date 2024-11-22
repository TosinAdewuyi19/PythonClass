from unittest import TestCase
import factorial

class TestFacttrialFunction(TestCase):
    def test_that_factorial_function_exists(self):
        number = [5]
        factorial.factorial(number)

    def test_that_factorial_function_returns_correct_value(self):
        numbers = [5]
        actual = factorial.factorial(numbers)
        expected = 120
        self.assertEqual(actual, expected)

