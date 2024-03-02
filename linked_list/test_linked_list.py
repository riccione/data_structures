"""
Tests for Singly Linked List

Inspired by William Fiset
https://github.com/williamfiset/

William wrote tests for double linked list, I was lazy and wrote simple singly
linked list.
TODO: implement double linked list :/
"""
import unittest
from singly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def tearDown(self):
        self.ll = None

    def test_empty_list(self):
        list = LinkedList()
        self.assertTrue(list.is_empty())
        self.assertEqual(list.size(), 0)

    def test_remove_first_of_empty(self):
        list = LinkedList()
        with self.assertRaises(ValueError):
            list.pop_front()

    def test_remove_last_of_empty(self):
        with self.assertRaises(ValueError):
            self.ll.pop_back()

    def test_peek_first_of_empty(self):
        with self.assertRaises(ValueError):
            self.ll.peek_first()

    def test_peek_last_of_empty(self):
        with self.assertRaises(ValueError):
            self.ll.peek_last()

    def test_add_first(self):
        self.ll.push_front(3)
        self.assertEqual(self.ll.size(), 1)
        self.ll.push_front(5)
        self.assertEqual(self.ll.size(), 2)

    def test_add_last(self):
        self.ll.push_back(3)
        self.assertEqual(self.ll.size(), 1)
        self.ll.push_back(5)
        self.assertEqual(self.ll.size(), 2)

    def test_remove_first(self):
        self.ll.push_front(3)
        self.assertEqual(self.ll.pop_front(), 3)
        self.assertTrue(self.ll.is_empty())


if __name__ == "__main__":
    unittest.main()
