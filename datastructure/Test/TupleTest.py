import unittest
from datastructure.Tuple import Tuple

class TupleTest(unittest.TestCase):
    def setUp(self):
        self.tup = Tuple(1, 2, 3, 4, 5)

    def test_get(self):
        self.assertEqual(self.tup.get(2), 3)

    def test_length(self):
        self.assertEqual(self.tup.length(), 5)

    def test_index(self):
        self.assertEqual(self.tup.index(4), 3)

    def test_count(self):
        tup = Tuple(1, 2, 2, 3)
        self.assertEqual(tup.count(2), 2)

    def test_to_list(self):
        self.assertEqual(self.tup.to_list(), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

