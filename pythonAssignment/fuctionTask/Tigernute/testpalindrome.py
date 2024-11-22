from unittest import TestCase
import palindrome

class TestIsPalindromeFunction(TestCase):
    def test_that_is_palindrome_function_exists(self):
        string = ["madam"]
        palindrome.is_palindrome(string)

