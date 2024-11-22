from unittest import TestCase
import sum

class TestSumFunction(TestCase):
    def test_that_get_sum_function_exists(self):
        numbers = [2,3,5,6,8,]
        sum.get_sum(numbers)
    def test_that_get_sum_function_returns_correct_value(self):
        numbers = [2,3,5,6,8]
        actual = sum.get_sum(numbers)
        expected = 16
        self.assertEqual(actual, expected)

    

