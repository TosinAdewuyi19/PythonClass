from unittest import TestCase
import primenumber

class TestPrimenumberFunction(TestCase):
    def test_that_get_prime_number_function_exists(self):
        number = (7)
        primenumber.get_prime_number(number)

    def test_that_get_prime_number_function_returns_correct_value(self):
        actual = primenumber.get_prime_number(7)
        expected = False
        self.assertEqual(actual, expected)

