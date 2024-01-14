"""
Fenwick Tree = Binary Indexed Tree

Inspired by William Fiset
https://github.com/williamfiset/
"""

import unittest
from fenwick_tree import FenwickTree
import random


class TestFenwickTree(unittest.TestCase):
    MIN_RAND_NUM = -1000
    MAX_RAND_NUM = 1000
    TEST_SZ = 1000
    LOOPS = 1000

    UNUSED_VAL = 0

    def setUp(self):
        self.UNUSED_VAL = self.rand_value()

    def rand_value(self) -> int:
        return int(random.random() * self.MAX_RAND_NUM * 2) + self.MIN_RAND_NUM

    def test_interval_sum_positive_values(self):
        vs = [self.UNUSED_VAL, 1, 2, 3, 4, 5, 6]
        ft = FenwickTree(values=vs)
        # print(ft)

        self.assertEqual(ft.sum_(1, 6), 21)
        self.assertEqual(ft.sum_(1, 5), 15)
        self.assertEqual(ft.sum_(1, 4), 10)
        self.assertEqual(ft.sum_(1, 3), 6)
        self.assertEqual(ft.sum_(1, 2), 3)
        self.assertEqual(ft.sum_(1, 1), 1)

        self.assertEqual(ft.sum_(3, 4), 7)
        self.assertEqual(ft.sum_(2, 6), 20)
        self.assertEqual(ft.sum_(4, 5), 9)
        self.assertEqual(ft.sum_(6, 6), 6)
        self.assertEqual(ft.sum_(5, 5), 5)
        self.assertEqual(ft.sum_(4, 4), 4)
        self.assertEqual(ft.sum_(3, 3), 3)
        self.assertEqual(ft.sum_(2, 2), 2)
        self.assertEqual(ft.sum_(1, 1), 1)

    def test_interval_sum_negative_values(self):
        vs = [self.UNUSED_VAL, -1, -2, -3, -4, -5, -6]
        ft = FenwickTree(values=vs)

        self.assertEqual(ft.sum_(1, 6), -21)
        self.assertEqual(ft.sum_(1, 5), -15)
        self.assertEqual(ft.sum_(1, 4), -10)
        self.assertEqual(ft.sum_(1, 3), -6)
        self.assertEqual(ft.sum_(1, 2), -3)
        self.assertEqual(ft.sum_(1, 1), -1)

        self.assertEqual(ft.sum_(3, 4), -7)
        self.assertEqual(ft.sum_(2, 6), -20)
        self.assertEqual(ft.sum_(4, 5), -9)
        self.assertEqual(ft.sum_(6, 6), -6)
        self.assertEqual(ft.sum_(5, 5), -5)
        self.assertEqual(ft.sum_(4, 4), -4)
        self.assertEqual(ft.sum_(3, 3), -3)
        self.assertEqual(ft.sum_(2, 2), -2)
        self.assertEqual(ft.sum_(1, 1), -1)

    def test_interval_sum_negative_values2(self):
        vs = [self.UNUSED_VAL, -76871, -164790]
        ft = FenwickTree(values=vs)

        for i in range(self.LOOPS):
            self.assertEqual(ft.sum_(1, 1), -76871)
            self.assertEqual(ft.sum_(1, 1), -76871)
            self.assertEqual(ft.sum_(1, 2), -241661)
            self.assertEqual(ft.sum_(1, 2), -241661)
            self.assertEqual(ft.sum_(2, 2), -164790)
            self.assertEqual(ft.sum_(2, 2), -164790)

    def test_randomized_static_sum_queries(self):
        for i in range(1, self.LOOPS):
            rl = self.get_rand_list(i)
            ft = FenwickTree(values=rl)

            for j in range(int(self.LOOPS / 10)):
                self.do_random_range_query(rl, ft)

    def do_random_range_query(self, rl, ft):
        sum_ = 0
        N = len(rl) - 1
        lo = self.low_bound(N)
        hi = self.high_bound(lo, N)
        # TODO need to investigate and understand why I get hi < lo
        if hi >= lo:
            i = lo
            while i <= hi:
                sum_ += rl[i]
                i += 1
                # print(i, rl)

            self.assertEqual(ft.sum_(lo, hi), sum_)

    def test_randomized_set_sum_queries(self):
        for i in range(2, self.LOOPS):
            rl = self.get_rand_list(i)
            ft = FenwickTree(values=rl)

            for j in range(int(self.LOOPS / 10)):
                index = (1 + int(random.random() * i)) % i
                if index > 0:
                    rand_val = self.rand_value()
                    # breakpoint()
                    rl[index] += rand_val
                    # breakpoint()
                    ft.add(index, rand_val)

                    # print(f"i = {i}, rl = {rl}, index = {index}")

                    self.do_random_range_query(rl, ft)

    def test_reusability(self):
        s = 2
        ft = FenwickTree(sz=s)
        arr = (s + 1) * [0]
        for i in range(self.LOOPS):
            for j in range(1, s):
                v = self.rand_value()
                print(ft, j, v)
                ft.set_(j, v)
                arr[j] = v
            self.do_random_range_query(arr, ft)

    def low_bound(self, n):
        return 1 + int(random.random() * n)

    def high_bound(self, low, n):
        return min(n, low + int(random.random() * n))

    def get_rand_list(self, sz: int):
        l = []
        for i in range(sz):
            l.append(self.rand_value())
        return l

    def test_create_invalid_ft(self):
        with self.assertRaises(ValueError):
            ft = FenwickTree(sz=None)

    def test_create_empty_ft(self):
        ft = FenwickTree()
        self.assertTrue(ft.N, 2)


if __name__ == "__main__":
    unittest.main()
