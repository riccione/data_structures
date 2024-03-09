"""
Tests for Binary Search Tree (BST)

Inspired by William Fiset
https://github.com/williamfiset/
"""

import unittest
from bst import BinarySearchTree

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

if __name__ == '__main__':
    unittest.main()
