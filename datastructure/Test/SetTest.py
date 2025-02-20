import unittest
from datastructure.Set import Set

class TestSet(unittest.TestCase):
    def setUp(self):
        self.set_a = Set([1, 2, 3])
        self.set_b = Set([3, 4, 5])

    def test_add(self):
        self.set_a.add(4)
        self.assertTrue(self.set_a.contains(4))

    def test_remove(self):
        self.set_a.remove(2)
        self.assertFalse(self.set_a.contains(2))

    def test_contains(self):
        self.assertTrue(self.set_a.contains(3))
        self.assertFalse(self.set_a.contains(99))

    def test_union(self):
        result = self.set_a.union(self.set_b)
        self.assertEqual(sorted(result.set), [1, 2, 3, 4, 5])

    def test_intersection(self):
        result = self.set_a.intersection(self.set_b)
        self.assertEqual(result.set, [3])

    def test_difference(self):
        result = self.set_a.difference(self.set_b)
        self.assertEqual(sorted(result.set), [1, 2])

    def test_is_subset(self):
        subset = Set([1, 2])
        self.assertTrue(subset.is_subset(self.set_a))
        self.assertFalse(self.set_b.is_subset(self.set_a))

if __name__ == '__main__':
    unittest.main()


