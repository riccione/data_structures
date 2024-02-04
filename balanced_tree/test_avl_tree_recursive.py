"""
Tests for AVL Tree

Inspired by William Fiset
https://github.com/williamfiset/
"""
import unittest
import math
import random
from avl_tree_recursive import AVLTreeRecursive


class TestAVLTree(unittest.TestCase):
    MAX_RAND_NUM = 100000
    MIN_RAND_NUM = -100000
    TEST_SZ = 2500

    def setUp(self):
        self.tree = AVLTreeRecursive()

    def test_null_insertion(self):
        self.assertFalse(self.tree.insert(None))

    def test_null_removal(self):
        self.assertFalse(self.tree.remove(None))

    def test_tree_contains_null(self):
        self.assertFalse(self.tree.contains(None))

    def test_left_left_case(self):
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(1)

        self.assertEqual(self.tree.root.value, 2)
        self.assertEqual(self.tree.root.left.value, 1)
        self.assertEqual(self.tree.root.right.value, 3)

        self.assertEqual(self.tree.root.left.left, None)
        self.assertEqual(self.tree.root.left.right, None)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)

    def test_left_right_case(self):
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.insert(2)

        self.assertEqual(self.tree.root.value, 2)
        self.assertEqual(self.tree.root.left.value, 1)
        self.assertEqual(self.tree.root.right.value, 3)

        self.assertEqual(self.tree.root.left.left, None)
        self.assertEqual(self.tree.root.left.right, None)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)

    def test_right_right_case(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(3)

        self.assertEqual(self.tree.root.value, 2)
        self.assertEqual(self.tree.root.left.value, 1)
        self.assertEqual(self.tree.root.right.value, 3)

        self.assertEqual(self.tree.root.left.left, None)
        self.assertEqual(self.tree.root.left.right, None)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)

    def test_right_left_case(self):
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(2)

        self.assertEqual(self.tree.root.value, 2)
        self.assertEqual(self.tree.root.left.value, 1)
        self.assertEqual(self.tree.root.right.value, 3)

        self.assertEqual(self.tree.root.left.left, None)
        self.assertEqual(self.tree.root.left.right, None)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)

    def test_randomized_bf(self):
        for i in range(self.TEST_SZ):
            self.tree.insert(self.rand_value())
            self.assertTrue(self.validate_bf(self.tree.root))

    def rand_value(self):
        return random.randint(self.MIN_RAND_NUM, self.MAX_RAND_NUM)

    def validate_bf(self, node):
        if node is None:
            return True
        if node.bf > 1 or node.bf < -1:
            return False
        return self.validate_bf(node.left) and self.validate_bf(node.right)

    def test_randomized_value_insertions_against_set(self):
        s = set()
        for i in range(self.TEST_SZ):
            v = self.rand_value()

            # won't work True != None, set does not return bool
            # self.assertEqual(self.tree.insert(v), s.add(v))
            self.tree.insert(v)
            s.add(v)
            self.assertEqual(self.tree.size(), len(s))
            self.assertTrue(self.tree.validate_bst_invariant(self.tree.root))

    def test_tree_height(self):
        for i in range(self.TEST_SZ):
            self.tree.insert(self.rand_value())
            height = self.tree.height()

            # get upper bound on what the max height of AVL
            # values are taken from https://en.wikipedia.org/wiki/AVL_tree#Comparison_to_other_structures
            c = 1.441
            b = -0.329
            upper_bound = c * (math.log(i + 2.0) / math.log(2)) + b

            self.assertLess(height, upper_bound)

    def test_random_remove(self):
        ts = set()
        for i in range(self.TEST_SZ):
            size = i
            lst = self.get_rand_lst(size)
            for v in lst:
                self.tree.insert(v)
                ts.add(v)
            random.shuffle(lst)

            # remove all elements
            for j in range(size):
                v = lst[j]

                self.tree.remove(v)
                ts.remove(v)

                self.assertFalse(self.tree.contains(v))

    def get_rand_lst(self, sz):
        lst = []
        for i in range(sz):
            lst.append(i)
        random.shuffle(lst)
        return lst


if __name__ == "__main__":
    unittest.main()
