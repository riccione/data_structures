import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_empty_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)

    def test_deque_on_empty(self):
        q = Queue()
        with self.assertRaises(ValueError):
            q.deque()

    def test_peek_on_empty(self):
        q = Queue()
        with self.assertRaises(ValueError):
            q.deque()

    def test_enque(self):
        q = Queue()
        q.enque(2)
        self.assertEqual(q.size(), 1)

    def test_peek(self):
        q = Queue()
        q.enque(2)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.size(), 1)

    def test_deque(self):
        q = Queue()
        q.enque(2)
        self.assertEqual(q.deque(), 2)
        self.assertEqual(q.size(), 0)

    def test_all(self):
        q = Queue()
        loops = 100
        self.assertTrue(q.is_empty())

        for i in range(loops):
            q.enque(i)

        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), loops)

        print(q)

        self.assertEqual(q.peek(), 0)
        self.assertEqual(q.size(), loops)

        for i in range(loops):
            self.assertEqual(q.deque(), i)
            self.assertEqual(q.size(), loops - 1 - i)

        self.assertEqual(q.size(), 0)


if __name__ == "__main__":
    unittest.main()
