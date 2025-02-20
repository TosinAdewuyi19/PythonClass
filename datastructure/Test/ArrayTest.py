import unittest
from datastructure.Array import Array


class TestArrayMethods(unittest.TestCase):
    def setUp(self):
        self.arr = Array([1, 2, 3, 4, 5])

    def test_append(self):
        self.arr.append(6)
        self.assertEqual(self.arr.arr, [1, 2, 3, 4, 5, 6])

    def test_insert(self):
        self.arr.insert(2, 99)
        self.assertEqual(self.arr.arr, [1, 2, 99, 3, 4, 5])

    def test_remove(self):
        self.arr.remove(3)
        self.assertEqual(self.arr.arr, [1, 2, 4, 5])

    def test_pop(self):
        value = self.arr.pop()
        self.assertEqual(value, 5)
        self.assertEqual(self.arr.arr, [1, 2, 3, 4])

    def test_sort(self):
        self.arr.arr = [3, 1, 4, 2]
        self.arr.sort()
        self.assertEqual(self.arr.arr, [1, 2, 3, 4])

    def test_reverse(self):
        self.arr.reverse()
        self.assertEqual(self.arr.arr, [5, 4, 3, 2, 1])

    def test_index(self):
        self.assertEqual(self.arr.index(4), 3)

    def test_count(self):
        self.arr.append(1)
        self.assertEqual(self.arr.count(1), 2)

    def test_slice(self):
        self.assertEqual(self.arr.slice(1, 4), [2, 3, 4])

if __name__ == '__main__':
    unittest.main()

