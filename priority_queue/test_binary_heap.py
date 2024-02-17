"""
Tests for Priority Queue

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""
import unittest
import random
import heapq

# PriorityQueue uses internally heapq, and it's thread safe
# https://stackoverflow.com/questions/36991716/whats-the-difference-between-heapq-and-priorityqueue-in-python
from queue import PriorityQueue
from binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    LOOPS = 100
    MAX_SZ = 100

    def test_empty(self):
        q = BinaryHeap()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.poll(), None)
        self.assertEqual(q.peek(), None)

    def test_heap_property(self):
        q = BinaryHeap()
        n = [3, 2, 5, 6, 7, 9, 4, 8, 1]

        # manually creating heap
        for x in n:
            q.add(x)
        for i in range(1, 10):
            self.assertEqual(q.poll(), i)
        q.clear()

        # try heapify
        q = BinaryHeap(n)
        for i in range(1, 10):
            self.assertEqual(q.poll(), i)

    def test_heapify(self):
        for i in range(1, self.LOOPS):
            lst = self.gen_rand_array(i)
            pq = BinaryHeap(lst)
            pq2 = []
            for x in lst:
                heapq.heappush(pq2, x)

            self.assertTrue(pq.is_min_heap(0))

            while len(pq2) > 0:
                self.assertEqual(pq.poll(), heapq.heappop(pq2))

    def test_clear(self):
        lst = ["aa", "bb", "cc", "dd", "ee"]
        q = BinaryHeap(lst)
        q.clear()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_containment(self):
        lst = ["aa", "bb", "cc", "dd", "ee"]
        q = BinaryHeap(lst)
        for x in lst:
            q.remove(x)
            self.assertFalse(q.contains(x))
        q.clear()
        self.assertFalse(q.contains("ee"))

    def test_containment_randomized(self):
        for i in range(self.LOOPS):
            rand_nums = self.gen_rand_array(self.LOOPS)
            h = []
            pq = BinaryHeap()
            for x in rand_nums:
                heapq.heappush(h, x)
                pq.add(x)

            for x in rand_nums:
                rand_val = x
                self.assertEqual(pq.contains(x), x in h)
                pq.remove(x)
                h.remove(x)
                self.assertEqual(pq.contains(x), x in h)

    def sequential_removing(self, in_, remove_order):
        self.assertEqual(len(in_), len(remove_order))

        pq = BinaryHeap(in_)
        h = list(in_)  # create a copy
        heapq.heapify(h)

        for el in remove_order:
            self.assertEqual(pq.peek(), h[0])
            pq.remove(el)
            h.remove(el)
            self.assertEqual(pq.size(), len(h))
            self.assertTrue(pq.is_min_heap(0))

        self.assertTrue(pq.is_empty())

    def test_removing(self):
        in_ = [1, 2, 3, 4, 5, 6, 7]
        remove_order = [1, 3, 6, 4, 5, 7, 2]
        self.sequential_removing(in_, remove_order)

        in_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        remove_order = [7, 4, 6, 10, 2, 5, 11, 3, 1, 8, 9]
        self.sequential_removing(in_, remove_order)

        in_ = [8, 1, 3, 3, 5, 3]
        remove_order = [3, 3, 5, 8, 1, 3]
        self.sequential_removing(in_, remove_order)

        in_ = [7, 7, 3, 1, 1, 2]
        remove_order = [2, 7, 1, 3, 7, 1]
        self.sequential_removing(in_, remove_order)

        in_ = [32, 66, 93, 42, 41, 91, 54, 64, 9, 35]
        remove_order = [64, 93, 54, 41, 35, 9, 66, 42, 32, 91]
        self.sequential_removing(in_, remove_order)

    def test_removing_duplicates(self):
        in_ = [2, 7, 2, 11, 7, 13, 2]
        pq = BinaryHeap(in_)

        self.assertEqual(pq.peek(), 2)
        pq.add(3)

        self.assertEqual(pq.poll(), 2)
        self.assertEqual(pq.poll(), 2)
        self.assertEqual(pq.poll(), 2)
        self.assertEqual(pq.poll(), 3)
        self.assertEqual(pq.poll(), 7)
        self.assertEqual(pq.poll(), 7)
        self.assertEqual(pq.poll(), 11)
        self.assertEqual(pq.poll(), 13)

    def test_randomized_polling(self):
        for i in range(self.LOOPS):
            sz = i
            rand_nums = self.gen_rand_array(sz)
            pq1 = []
            pq2 = BinaryHeap()

            # add all elements
            for v in rand_nums:
                heapq.heappush(pq1, v)
                pq2.add(v)

            while len(pq1) > 0:
                self.assertTrue(pq2.is_min_heap(0))
                self.assertEqual(len(pq1), pq2.size())
                self.assertEqual(pq1[0], pq2.peek())
                self.assertEqual(pq1[0] in pq1, pq2.contains(pq2.peek()))

                v1 = heapq.heappop(pq1)
                v2 = pq2.poll()

                self.assertEqual(v1, v2)
                if len(pq1) == 0:
                    break
                self.assertEqual(pq1[0], pq2.peek())
                self.assertEqual(len(pq1), pq2.size())
                self.assertTrue(pq2.is_min_heap(0))

    def test_randomized_removing(self):
        for i in range(self.LOOPS):
            sz = i
            rand_nums = self.gen_rand_array(sz)
            pq1 = []
            pq2 = BinaryHeap()

            # add all elements
            for v in rand_nums:
                heapq.heappush(pq1, v)
                pq2.add(v)

            while len(pq1) > 0:
                self.assertTrue(pq2.is_min_heap(0))
                self.assertEqual(len(pq1), pq2.size())
                self.assertEqual(pq1[0], pq2.peek())
                self.assertEqual(pq1[0] in pq1, pq2.contains(pq2.peek()))

                v1 = heapq.heappop(pq1)
                v2 = pq2.remove(pq2.peek())

                if v1 is not None:
                    v1 = True

                self.assertEqual(v1, v2)
                if len(pq1) == 0:
                    break
                self.assertEqual(pq1[0], pq2.peek())
                self.assertEqual(len(pq1), pq2.size())
                self.assertTrue(pq2.is_min_heap(0))

    def test_pq_reusability(self):
        xs = self.gen_unique_rand_list(self.LOOPS)

        pq1 = []
        pq2 = BinaryHeap()

        for x in xs:
            pq1.clear()
            pq2.clear()

            nums = self.gen_rand_array(x)
            for n in nums:
                heapq.heappush(pq1, n)
                pq2.add(n)

            random.shuffle(nums)

            for i in range(x // 2):
                if 0.25 < random.random():
                    rv = int(random.random() * 10000)
                    heapq.heappush(pq1, rv)
                    pq2.add(rv)

                remove_num = nums[i]

                self.assertTrue(pq2.is_min_heap(0))
                self.assertEqual(len(pq1), pq2.size())
                self.assertEqual(pq1[0], pq2.peek())

                pq1.remove(remove_num)
                heapq.heapify(pq1)
                pq2.remove(remove_num)

                self.assertEqual(pq1[0], pq2.peek())
                self.assertEqual(len(pq1), pq2.size())
                self.assertTrue(pq2.is_min_heap(0))

    def gen_rand_array(self, sz: int):
        lst = []
        for i in range(sz):
            lst.append(random.randint(0, self.MAX_SZ))
        return lst

    def gen_unique_rand_list(self, sz: int):
        lst = []
        for i in range(sz):
            lst.append(i)
        random.shuffle(lst)
        return lst


if __name__ == "__main__":
    unittest.main()
