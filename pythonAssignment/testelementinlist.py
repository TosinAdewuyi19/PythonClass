from unittest import TestCase
import elementexists

class element_exists_function(TestCase):
	def test_that_element_exists_function_exists(self):
		list = [2,1,4,3,6,5]
		element = 0
		elementexists.element_exists(list, element)
	def test_that_element_exists_function_treturns_correct_value(self):
		list = [2,1,4,3,6,5]
		element = 6
		actual = elementexists.element_exists(list, element)
		expected = 6
		self.assertEqual(actual, expected)
	
