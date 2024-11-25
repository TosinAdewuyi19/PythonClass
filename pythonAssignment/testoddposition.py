from unittest import TestCase
import oddposition

class print_odd_position_function(TestCase):
	def test_that_print_odd_position_function_exists(self):
		list = [10,15,25,20,30]
		oddposition.print_odd_position(list)
	def test_that_print_odd_position_function_retirn_correct_value(self):
		list = [10,15,25,20,30]
		actual = oddposition.print_odd_position(list)
		self.assertEqual(actual)

