from unittest import TestCase
import evenposition

class even_position_elements_function(TestCase):
	def test_that_even_position_elements_function_exists(self):
		list = [10,15,25,20,30]
		evenposition.even_position_elements(list)
	def test_that_even_position_elements_function_return_correct_value(self):
		list = [10,15,25,20,30]
		actual = evenposition.even_position_elements(list)
		expected = [10,25,30]
		self.assertEqual(actual, expected)
