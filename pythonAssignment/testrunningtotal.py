from unittest import TestCase
import runningtotal

class running_total_function(TestCase):
	def test_that_running_total_function_exists(self):
		list = [1,2,3,4,5]
		runningtotal.running_total(list)
	def test_that_running_total_function_teturns_correct_valeu(self):
		list = [1,2,3,4,5]
		total = 0
		actual = runningtotal.running_total(list)
		expected = [1,3,6,10,15]
		self.assertEqual(actual, expected)
 