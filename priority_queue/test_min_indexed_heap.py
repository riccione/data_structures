"""
Tests for Indexed Priority Queue

An implementation of an indexed binary heap priority queue.

This implementation supports arbitrary keys with comparable values. To use arbitrary keys
(such as strings or objects) first map all your keys to the integer domain [0, N) where N is the
number of keys you have and then use the mapping with this indexed priority queue.
 
As convention, I denote 'ki' as the index value in the domain [0, N) associated with key k,
therefore: ki = map[k]

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""

import random
from min_indexed_binary_heap import MinIndexedBinaryHeap
import unittest


class TestMinIndexedBinaryHeap(unittest.TestCase):
    def test_illegal_size_of_negative_one(self):
        with self.assertRaises(ValueError):
            MinIndexedBinaryHeap(-1)

    def test_illegal_size_of_zero(self):
        with self.assertRaises(ValueError):
            MinIndexedBinaryHeap(0)

    def test_legal_size(self):
        MinIndexedBinaryHeap(1)

    def test_contains_valid_key(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(5, "abcdef")
        self.assertTrue(pq.contains(5))

    def test_contains_invalid_key(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(5, "abcdef")
        self.assertFalse(pq.contains(3))

    def test_duplicate_keys(self):
        with self.assertRaises(ValueError):
            pq = MinIndexedBinaryHeap(10)
            pq.insert(5, "abcdef")
            pq.insert(5, "xyz")

    def test_update_key_value(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(5, "abcdef")
        pq.update(5, "xyz")
        self.assertEqual(pq.value_of(5), "xyz")

    def test_decrease_key(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(3, 5)
        pq.decrease(3, 4)
        self.assertEqual(pq.value_of(3), 4)

    def test_decrease_key_no_update(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(3, 5)
        pq.decrease(3, 6)
        self.assertEqual(pq.value_of(3), 5)

    def test_increase_key(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(3, 5)
        pq.increase(3, 6)
        self.assertEqual(pq.value_of(3), 6)

    def test_increase_key_no_update(self):
        pq = MinIndexedBinaryHeap(10)
        pq.insert(3, 5)
        pq.increase(3, 4)
        self.assertEqual(pq.value_of(3), 5)

    def test_peek_and_poll_min_index(self):
        pairs = [
            [4, 1],
            [7, 5],
            [1, 6],
            [5, 8],
            [3, 7],
            [6, 9],
            [8, 0],
            [2, 4],
            [9, 3],
            [0, 2],
        ]

        pairs = self.sort_pairs_by_value(pairs)

        n = len(pairs)
        pq = MinIndexedBinaryHeap(n)
        for x in pairs:
            pq.insert(x[0], x[1])

        for i in range(n):
            min_index = pq.peek_min_key_index()
            self.assertEqual(min_index, pairs[i][0])
            min_index = pq.poll_min_key_index()
            self.assertEqual(min_index, pairs[i][0])

    def test_peek_and_poll_min_value(self):
        pairs = [
            [4, 1],
            [7, 5],
            [1, 6],
            [5, 8],
            [3, 7],
            [6, 9],
            [8, 0],
            [2, 4],
            [9, 3],
            [0, 2],
        ]

        pairs = self.sort_pairs_by_value(pairs)

        n = len(pairs)
        pq = MinIndexedBinaryHeap(n)
        for x in pairs:
            pq.insert(x[0], x[1])

        for i in range(n):
            self.assertEqual(pq.value_of(pairs[i][0]), pairs[i][1])
            min_value = pq.peek_min_value()
            self.assertEqual(min_value, pairs[i][1])
            min_value = pq.poll_min_value()
            self.assertEqual(min_value, pairs[i][1])

    def test_insertion_and_value_of(self):
        names = ["jackie", "wilson", "catherine", "jason", "bobby", "sia"]
        pq = MinIndexedBinaryHeap(len(names))
        for i, x in enumerate(names):
            pq.insert(i, x)

        for i, x in enumerate(names):
            self.assertEqual(pq.value_of(i), x)

    def test_operations(self):
        n = 7
        pq = MinIndexedBinaryHeap(n)

        pq.insert(4, 4)
        self.assertTrue(pq.contains(4))
        self.assertEqual(pq.peek_min_value(), 4)
        self.assertEqual(pq.peek_min_key_index(), 4)
        pq.update(4, 8)
        self.assertEqual(pq.peek_min_value(), 8)
        self.assertEqual(pq.poll_min_key_index(), 4)
        self.assertFalse(pq.contains(4))
        pq.insert(3, 99)
        pq.insert(1, 101)
        pq.insert(2, 60)
        self.assertEqual(pq.peek_min_value(), 60)
        self.assertEqual(pq.peek_min_key_index(), 2)
        pq.increase(2, 150)
        self.assertEqual(pq.peek_min_value(), 99)
        self.assertEqual(pq.peek_min_key_index(), 3)
        pq.increase(3, 250)
        self.assertEqual(pq.peek_min_value(), 101)
        self.assertEqual(pq.peek_min_key_index(), 1)
        pq.decrease(3, -500)
        self.assertEqual(pq.peek_min_value(), -500)
        self.assertEqual(pq.peek_min_key_index(), 3)
        self.assertTrue(pq.contains(3))
        pq.delete(3)
        self.assertFalse(pq.contains(3))
        self.assertEqual(pq.peek_min_value(), 101)
        self.assertEqual(pq.peek_min_key_index(), 1)
        self.assertEqual(pq.value_of(1), 101)

    def test_random_insertions_and_polls(self):
        # TODO: implement
        pass

    def sort_pairs_by_value(self, pairs):
        return sorted(pairs, key=lambda x: x[1])


if __name__ == "__main__":
    unittest.main()
