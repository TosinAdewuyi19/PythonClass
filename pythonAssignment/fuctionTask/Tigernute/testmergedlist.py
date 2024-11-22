from unittest import TestCase
import mergedlist

class TestMergedListFunction(TestCase):
    def test_that_get_merged_function_exists(self):
        list_one = [1,3,5]
        list_two = [2,4,6]
        mergedlist.get_merged(list_one, list_two)

    def test_that_get_merged_function_returns_correct_value(self):
        list_one = [1,3,5]
        list_two = [2,4,6]
        actual = mergedlist.get_merged(list_one, list_two)
        expected = [1,2,3,4,5,6]
        self.assertEqual(actual, expected)

