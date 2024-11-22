from unittest import TestCase
import gettotal

class TestgetTotalFunction(TestCase):
    def test_that_get_total_function_exists(self):
        numbers = [1,5,3,2,4]
        gettotal.get_total(numbers)

    def test_that_get_total_function_returns_correct_value(self):
        numbers = [1,5,3,2,4]
        actual = gettotal.get_total(numbers)
        expected = 15
        self.assertEqual(actual, expected)

