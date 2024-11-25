from unittest import TestCase
import largestelement

class get_largest_element_Function(TestCase):
	def test_that_get_largest_elementfunction_exists(self):
		element = {20,10,25,40}
		largestelement.get_largest_element(element)

	def test_that_get_largest_element_function_returns_correct_value(self):
		element = {20,10,25,40}
		actual = largestelement.get_largest_element(element)
		expected = 40
		self.assertEqual(actual, expected)
	
