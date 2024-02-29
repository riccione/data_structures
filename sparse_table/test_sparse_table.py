"""
Tests for Sparse Table

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""

import unittest
import random
from sparse_table import SparseTable
from sparse_table import Operation


class TestSparseTable(unittest.TestCase):
    def test_simple(self):
        values = [1, 0, 1, -2, 3, -4, 5, -6, 7, -8, 9]
        self.all_operations(values)

    def test_small_range_random_array(self):
        for i in range(1, 100):
            xs = self.gen_rand_array(i, -10, 10)
            self.all_operations(xs)

    def test_random_array(self):
        for i in range(1, 100):
            xs = self.gen_rand_array(i, -100000, 100000)
            self.all_operations(xs)

    # verify index is always left most position when there are  collisions
    def test_verify_index_is_always_leftmost(self):
        xs = [5, 4, 3, 3, 3, 3, 3, 5, 6, 7]
        st = SparseTable(xs, Operation.MIN)

        for i in range(len(xs)):
            for j in range(i, len(xs)):
                min_ = float("inf")
                min_index = 0
                for k in range(i, j + 1):
                    if xs[k] < min_:
                        min_ = xs[k]
                        min_index = k

                self.assertEqual(st.query_value(i, j), min_)
                self.assertTrue(i <= min_index and min_index <= j)
                self.assertEqual(st.query_index(i, j), min_index)

    def test_verify_index_is_always_leftmost_randomized(self):
        for loop in range(2, 100):
            xs = self.gen_rand_array(loop, -100, 100)
            min_st = SparseTable(xs, Operation.MIN)
            max_st = SparseTable(xs, Operation.MAX)

            for i in range(len(xs)):
                for j in range(i, len(xs)):
                    min_ = float("inf")
                    max_ = float("-inf")
                    min_index = 0
                    max_index = 0
                    for k in range(i, j + 1):
                        if xs[k] < min_:
                            min_ = xs[k]
                            min_index = k
                        if xs[k] > max_:
                            max_ = xs[k]
                            max_index = k

                    self.assertEqual(min_st.query_value(i, j), min_)
                    self.assertTrue(i <= min_index and min_index <= j)
                    self.assertEqual(min_st.query_index(i, j), min_index)

                    self.assertEqual(max_st.query_value(i, j), max_)
                    self.assertTrue(i <= max_index and max_index <= j)
                    self.assertEqual(max_st.query_index(i, j), max_index)

    def gen_rand_array(self, i, lo, hi):
        return [random.randint(lo, hi) for _ in range(i)]

    def all_operations(self, values):
        min_st = SparseTable(values, Operation.MIN)
        max_st = SparseTable(values, Operation.MAX)
        sum_st = SparseTable(values, Operation.SUM)
        mult_st = SparseTable(values, Operation.MULT)
        gcd_st = SparseTable(values, Operation.GCD)

        for i in range(len(values)):
            for j in range(i, len(values)):
                self.query_result(
                    values,
                    i,
                    j,
                    min_st.query_value(i, j),
                    min_st.query_index(i, j),
                    Operation.MIN,
                )
                self.query_result(
                    values,
                    i,
                    j,
                    max_st.query_value(i, j),
                    max_st.query_index(i, j),
                    Operation.MAX,
                )
                self.query_result(
                    values, i, j, sum_st.query_value(i, j), -1, Operation.SUM
                )
                self.query_result(
                    values, i, j, mult_st.query_value(i, j), -1, Operation.MULT
                )
                self.query_result(
                    values, i, j, gcd_st.query_value(i, j), -1, Operation.GCD
                )

    def query_result(self, v, l: int, r: int, actual: int, index: int, op):
        if op == Operation.MIN:
            self.min_query(v, l, r, actual, index)
        elif op == Operation.MAX:
            self.max_query(v, l, r, actual, index)
        elif op == Operation.SUM:
            self.sum_query(v, l, r, actual)
        elif op == Operation.MULT:
            self.mult_query(v, l, r, actual)
        else:  # Operation.GCD
            self.gcd_query(v, l, r, actual)

    def min_query(self, v, l: int, r: int, actual: int, index: int):
        m = float("inf")
        while l <= r:
            m = min(m, v[l])
            l += 1
        self.assertEqual(actual, m)
        self.assertEqual(v[index], m)

    def max_query(self, v, l: int, r: int, actual: int, index: int):
        m = float("-inf")
        for i in range(l, r + 1):
            m = max(m, v[i])
        self.assertEqual(actual, m)
        self.assertEqual(v[index], m)

    def sum_query(self, v, l: int, r: int, actual: int):
        m = 0
        for i in range(l, r + 1):
            m += v[i]
        self.assertEqual(actual, m)

    def mult_query(self, v, l: int, r: int, actual: int):
        m = 1
        for i in range(l, r + 1):
            m *= v[i]
        self.assertEqual(actual, m)

    def gcd_query(self, v, l: int, r: int, actual: int):
        m = v[l]
        for i in range(l, r + 1):
            m = self._gcd(m, v[i])
        self.assertEqual(actual, m)

    def _gcd(self, a, b):
        return abs(a) if b == 0 else self._gcd(b, a % b)


if __name__ == "__main__":
    unittest.main()
