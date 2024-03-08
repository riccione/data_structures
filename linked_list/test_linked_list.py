"""
Tests for Singly Linked List

Inspired by William Fiset
https://github.com/williamfiset/

William wrote tests for double linked list, I was lazy and wrote simple singly
linked list.
TODO: implement double linked list :/
"""
import unittest
import random
from singly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    LOOPS = 10000
    TEST_SZ = 40
    MAX_RAND_NUM = 250
    NUM_NULLS = TEST_SZ // 5

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

    def test_add_at(self):
        self.ll.push(0, 1)
        self.assertEqual(self.ll.size(), 1)
        self.ll.push(1, 2)
        self.assertEqual(self.ll.size(), 2)
        self.ll.push(1, 3)
        self.assertEqual(self.ll.size(), 3)
        self.ll.push(2, 4)
        self.assertEqual(self.ll.size(), 4)
        self.ll.push(1, 8)
        self.assertEqual(self.ll.size(), 5)

    def test_peek_first(self):
        self.ll.push_back(4)
        self.assertEqual(self.ll.peek_first(), 4)
        self.assertEqual(self.ll.size(), 1)

    def test_peek_last(self):
        self.ll.push_back(4)
        self.assertEqual(self.ll.peek_last(), 4)
        self.assertEqual(self.ll.size(), 1)

    def test_peeking(self):
        for i in range(10):
            self.ll.push_front(i)
            self.assertEqual(self.ll.peek_first(), i)
            self.assertEqual(self.ll.peek_last(), 0)

    def test_removing(self):
        self.ll.push_front("a")
        self.ll.push_front("b")
        self.ll.push_front("c")
        self.ll.push_front("d")
        self.ll.push_front("e")
        self.ll.push_front("f")
        self.ll.remove("b")
        self.ll.remove("a")
        self.ll.remove("d")
        self.ll.remove("e")
        self.ll.remove("c")
        self.ll.remove("f")
        self.assertEqual(self.ll.size(), 0)

    def test_remove_at(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.push_back(4)
        self.ll.remove_at(0)
        self.ll.remove_at(2)
        self.assertEqual(self.ll.peek_first(), 2)
        self.assertEqual(self.ll.peek_last(), 3)
        print(self.ll)
        self.ll.remove_at(1)
        self.ll.remove_at(0)
        self.assertEqual(self.ll.size(), 0)

    def test_clear(self):
        self.ll.push_front(22)
        self.ll.push_front(33)
        self.ll.push_front(44)
        self.assertEqual(self.ll.size(), 3)
        self.ll.clear()
        self.assertEqual(self.ll.size(), 0)
        self.ll.push_front(22)
        self.ll.push_front(33)
        self.ll.push_front(44)
        self.assertEqual(self.ll.size(), 3)
        self.ll.clear()
        self.assertEqual(self.ll.size(), 0)

    def test_randomized_removing(self):
        ll = []
        for loops in range(self.LOOPS):
            self.ll.clear()
            ll.clear()

            rand_nums = self.gen_rand_list(self.TEST_SZ)
            for x in rand_nums:
                self.ll.push_back(x)
                ll.append(x)

            random.shuffle(rand_nums)

            for i in range(len(rand_nums)):
                rm_val = rand_nums[i]
                self.assertEqual(self.ll.remove(rm_val), ll.pop(ll.index(rm_val)))
                self.assertEqual(self.ll.size(), len(ll))

    def test_randomized_remove_at(self):
        ll = []
        for loops in range(self.LOOPS):
            self.ll.clear()
            ll.clear()

            rand_nums = self.gen_rand_list(self.TEST_SZ)
            for x in rand_nums:
                self.ll.push_back(x)
                ll.append(x)

            for i in range(len(rand_nums)):
                rm_index = int(len(ll) * random.random())

                self.assertEqual(self.ll.remove_at(rm_index), ll.pop(rm_index))
                self.assertEqual(self.ll.size(), len(ll))

    def test_randomized_index_of(self):
        ll = []
        for loops in range(self.LOOPS):
            self.ll.clear()
            ll.clear()

            rand_nums = self.gen_unique_rand_list(self.TEST_SZ)
            for x in rand_nums:
                self.ll.push_back(x)
                ll.append(x)

            random.shuffle(rand_nums)

            for i in range(len(rand_nums)):
                el = rand_nums[i]

                index1 = self.ll.index_of(el)
                index2 = ll.index(el)

                self.assertEqual(index1, index2)
                self.assertEqual(self.ll.size(), len(ll))

    def gen_rand_list(self, sz):
        return [
            random.randint(-self.MAX_RAND_NUM, self.MAX_RAND_NUM) for _ in range(sz)
        ]

    def gen_unique_rand_list(self, sz):
        return [
            random.randint(-self.MAX_RAND_NUM, self.MAX_RAND_NUM) for _ in range(sz)
        ]


if __name__ == "__main__":
    unittest.main()
