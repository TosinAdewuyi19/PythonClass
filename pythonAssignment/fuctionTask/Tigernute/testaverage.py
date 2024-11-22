from unittest import TestCase
import average

class TestGetAverageFunction(TestCase):
    def test_that_get_average_function_exists(self):
        numbers = [10,20,30,40]
        average.get_average(numbers)

    def test_that_get_average_function_returns_correct_value(self):
        numbers = [10,20,30,40]
        actual = average.get_average (numbers)
        expected = 25.0
        self.assertEqual(actual, expected)


