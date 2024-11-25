from unittest import TestCase
import reverselist

class reverse_list_Function(TestCase):
	def test_that_reverse_list_function_exists(self):
		list = {1,2,3,4,5,6,7}
		reverselist.reverse_list(list)
	def test_that_reverse_list_function_returns_correct_value(self):
		list = {1,2,3,4,5,6,7}
		actual = reverselist.reverse_list(list)
		expected = [7,6,5,4,3,2,1]
		self.assertEqual(actual, expected)
