"""
Tests for Priority Queue

Inspired by Willam Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""
import unittest
from pq import BinaryHeap

class TestBinaryHeap(unittest.TestCase):

    LOOPS = 100
    MAX_SZ = 100

    def test_empty(self):
       q = BinaryHeap()
       self.assertEqual(q.size(), 0)

if __name__ == "__main__":
    unittest.main() 
