import unittest
from datastructure.Queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.queue, [1, 2])

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        value = self.queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(self.queue.queue, [2])

    def test_peek(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 3)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(4)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)




if __name__ == '__main__':
    unittest.main()
