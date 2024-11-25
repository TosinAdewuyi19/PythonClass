from unittest import TestCase
import concatenatedlist

class concatenated_list_function(TestCase):
	def test_that_concatenated_list_function_exists(self):
		list1 = ['a', 'b', 'c'] 
		list2 = [1, 2, 3]
		concatenatedlist.concatenated_list(list1, list2)
	def test_that_concatenated_list_function_teturns_correct_valeu(self):
		list1 = [a,b,c] 
		list2 = [1,2,3]
		actual = concatenatedlist.concatenated_list (list1, list2)
		expected = [a,b,c,1,2,3]
		self.assertEqual(actual, expected)

