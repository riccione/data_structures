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

    # in this test I don't use Binary Search Tree
    # it is just Binary Tree - this is done for simplicity
    def test_simple_tree_traversal(self):
        x = BinarySearchTree()
        x.add(1)
        x._add(x.root, 2, "left")
        x._add(x.root.left, 4, "left")
        x._add(x.root.left, 5, "right")
        x._add(x.root, 3, "right")
        x._add(x.root.right, 6, "left")
        x._add(x.root.right, 7, "right")
        print(x)
        expected_inorder = [4, 2, 5, 1, 6, 3, 7]
        expected_preorder = [1, 2, 4, 5, 3, 6, 7]
        expected_postorder = [4, 5, 2, 6, 7, 3, 1]

        # self.tree.traverse(self.tree.root, Order.IN_ORDER)
        i = 0
        for c in x.iter_in(x.root, Order.IN_ORDER):
            self.assertEqual(c, expected_inorder[i])
            # print(c, end=" ")
            i += 1

        i = 0
        for c in x.iter_pre(x.root, Order.PRE_ORDER):
            self.assertEqual(c, expected_preorder[i])
            i += 1

        i = 0
        for c in x.iter_post(x.root, Order.POST_ORDER):
            self.assertEqual(c, expected_postorder[i])
            i += 1


if __name__ == "__main__":
    unittest.main()
