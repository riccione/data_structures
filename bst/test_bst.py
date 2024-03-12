"""
Tests for Binary Search Tree (BST)

Inspired by William Fiset
https://github.com/williamfiset/
"""

import unittest
import random
from bst import BinarySearchTree
from bst import Order


class TestBinarySearchTree(unittest.TestCase):
    LOOPS = 100

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_is_empty(self):
        tree = BinarySearchTree()
        self.assertTrue(tree.is_empty())

        tree.add("Hello World!")
        self.assertFalse(tree.is_empty())

    def test_size(self):
        self.assertEqual(self.tree.size(), 0)

        self.tree.add("Hello World!")
        self.assertEqual(self.tree.size(), 1)

    def test_height(self):
        # no tree
        self.assertEqual(self.tree.height(), 0)

        # layer one
        self.tree.add("M")
        self.assertEqual(self.tree.height(), 1)

        # layer two
        self.tree.add("J")
        self.assertEqual(self.tree.height(), 2)
        self.tree.add("S")
        self.assertEqual(self.tree.height(), 2)

        # layer tre
        self.tree.add("B")
        self.assertEqual(self.tree.height(), 3)
        self.tree.add("N")
        self.assertEqual(self.tree.height(), 3)
        self.tree.add("Z")
        self.assertEqual(self.tree.height(), 3)

        # layer quatro
        self.tree.add("A")
        self.assertEqual(self.tree.height(), 4)

        print(self.tree)

    def test_add(self):
        self.assertTrue(self.tree.add("A"))

        # add a duplicate
        self.assertFalse(self.tree.add("A"))

        # add a second el
        self.assertTrue(self.tree.add("B"))

    def test_remove(self):
        # try to remove non-existing el
        self.tree.add("A")
        self.assertEqual(self.tree.size(), 1)
        self.assertFalse(self.tree.remove("B"))
        self.assertEqual(self.tree.size(), 1)

        # try to remove existing el
        self.tree.add("B")
        self.assertEqual(self.tree.size(), 2)
        self.assertTrue(self.tree.remove("B"))
        self.assertEqual(self.tree.size(), 1)
        self.assertEqual(self.tree.height(), 1)

        # try to remove root
        self.assertTrue(self.tree.remove("A"))
        self.assertEqual(self.tree.size(), 0)
        self.assertEqual(self.tree.height(), 0)

    def test_contains(self):
        self.tree.add("B")
        self.tree.add("A")
        self.tree.add("C")

        # try looking for a non-existing el
        self.assertFalse(self.tree.contains("D"))

        # try looking for an existing el in root
        self.assertTrue(self.tree.contains("B"))

        # try looking for an existing el on left
        self.assertTrue(self.tree.contains("A"))

        # try looking for an existing el on right
        self.assertTrue(self.tree.contains("C"))

    def test_random_remove(self):
        for i in range(self.LOOPS):
            sz = i
            lst = self.gen_rand_list(sz)

            for v in lst:
                self.tree.add(v)

            random.shuffle(lst)

            for j in range(sz):
                x = lst[j]
                self.assertTrue(self.tree.remove(x))
                self.assertFalse(self.tree.contains(x))
                self.assertEqual(self.tree.size(), sz - j - 1)

            self.assertTrue(self.tree.is_empty())

    def gen_rand_list(self, sz):
        lst = [i for i in range(sz)]
        random.shuffle(lst)
        return lst

    def test_simple_tree_traversal(self):
        # TODO: implement
        self.tree.add(1)
        self.tree.add(5)
        self.tree.add(2)
        self.tree.add(3)
        self.tree.add(6)
        # self.tree.add(2)
        # self.tree.add(7)
        print(self.tree)
        expected = [4, 2, 5, 1, 6, 3, 7]

        self.tree.traverse(self.tree.root, Order.IN_ORDER)


if __name__ == "__main__":
    unittest.main()
