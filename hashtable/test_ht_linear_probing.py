"""
HashTable Open Addressing: Linear Probing

Inspired by William Fiset
https://github.com/williamfiset/
"""
import random
import unittest
from ht_linear_probing import HashTableLinearProbing


class TestHTLinearProbing(unittest.TestCase):
    class HashObject:
        chash = None
        data = None

        def __init__(self, chash, data):
            self.chash = chash
            self.data = data

        def hash_code(self) -> int:
            return self.chash

    LOOPS = 500
    MAX_SIZE = random.randint(1, 750)
    MAX_RAND_NUM = random.randint(1, 350)
    ht = None

    def setUp(self):
        self.ht = HashTableLinearProbing()

    def test_none_key(self):
        with self.assertRaises(ValueError):
            self.ht.put(None, 5)

    def test_illegal_creation1(self):
        with self.assertRaises(ValueError):
            HashTableLinearProbing(capacity=-3, load_factor=0.5)

    def test_illegal_creation2(self):
        with self.assertRaises(ValueError):
            HashTableLinearProbing(capacity=6, load_factor=-0.5)

    def test_legal_creation(self):
        try:
            HashTableLinearProbing(capacity=6, load_factor=0.9)
        except ValueError:
            self.fail("ValueError")

    def test_update_value(self):
        self.ht.add(1, 1)
        self.assertEqual(self.ht.get(1), 1)

        self.ht.add(1, 5)
        self.assertEqual(self.ht.get(1), 5)

        self.ht.add(1, -7)
        self.assertEqual(self.ht.get(1), -7)

        self.ht.add(2, 2)
        self.assertEqual(self.ht.get(1), -7)

    def test_iterator(self):
        ht2 = HashTableLinearProbing()
        for i in range(self.LOOPS):
            self.ht.clear()
            ht2.clear()
            self.assertTrue(self.ht.is_empty())

            rand_nums = self.get_rand_list(self.MAX_SIZE)
            for k in rand_nums:
                self.assertEqual(self.ht.add(k, k), ht2.put(k, k))

            # breakpoint()
            count = 0
            for x in self.ht:
                self.assertEqual(self.ht.get(x), x)
                self.assertEqual(self.ht.get(x), ht2.get(x))
                self.assertTrue(self.ht.has_key(x))
                self.assertTrue(self.ht.contains(x))
                count += 1

            for x in ht2:
                self.assertEqual(self.ht.get(x), x)

            # need to be set, because get_rand_list generates duplicates
            # HashTable does not allow duplicates :) had a lot of troubles with
            # this test
            ss = set()
            for x in rand_nums:
                ss.add(x)

            self.assertEqual(len(ss), count)
            self.assertEqual(ht2.size(), count)

    # TODO: implement concurent tests

    def test_random_remove(self):
        for i in range(1):  # (self.LOOPS):
            ht = HashTableLinearProbing()
            ht.clear()

            keys_set = set()
            for i in range(self.MAX_SIZE):
                random_k = random.randint(-self.MAX_RAND_NUM, self.MAX_RAND_NUM)
                keys_set.add(random_k)
                ht.put(random_k, 5)

            self.assertEqual(ht.size(), len(keys_set))

            keys = [x for x in ht.keys if x is not None]
            for k in keys:
                ht.remove(k)

            self.assertTrue(ht.is_empty())

    def test_remove(self):
        ht = HashTableLinearProbing()
        ht.put(11, 0)
        ht.put(12, 0)
        ht.put(13, 0)
        self.assertEqual(ht.size(), 3)

        # add ten more
        for i in range(10):
            ht.put(i, 0)

        # remove ten
        for i in range(10):
            ht.remove(i)

        self.assertEqual(ht.size(), 3)

        # remove the rest
        ht.remove(11)
        ht.remove(12)
        ht.remove(13)
        self.assertEqual(ht.size(), 0)

    def test_remove_complex(self):
        ht = HashTableLinearProbing()
        o1 = self.HashObject(88, 1)
        o2 = self.HashObject(88, 2)
        o3 = self.HashObject(88, 3)
        o4 = self.HashObject(88, 4)
        ht.add(o1, 111)
        ht.add(o2, 111)
        ht.add(o3, 111)
        ht.add(o4, 111)

        ht.remove(o2)
        self.assertEqual(ht.size(), 3)
        ht.remove(o1)
        ht.remove(o3)
        ht.remove(o4)

        self.assertEqual(ht.size(), 0)
        self.assertTrue(ht.is_empty())

    def test_random_map_operations(self):
        d = {}

        for i in range(self.LOOPS):
            ht = HashTableLinearProbing()
            d.clear()

            probability1 = random.random()
            probability2 = random.random()

            nums = self.get_rand_list(self.MAX_SIZE)
            for i in range(self.MAX_SIZE):
                r = random.random()

                key = nums[i]
                val = i

                if r < probability1:
                    val1 = d[key] = val
                    val2 = ht.put(key, val)
                    self.assertEqual(val1, val2)

                self.assertEqual(d.get(key), ht.get(key))
                self.assertEqual(key in d, ht.contains(key))
                self.assertEqual(len(d), ht.size())

                if r > probability2:
                    val1 = d[key] = val
                    val2 = ht.put(key, val)
                    self.assertEqual(val1, val2)

                self.assertEqual(d.get(key), ht.get(key))
                self.assertEqual(key in d, ht.contains(key))
                self.assertEqual(len(d), ht.size())

    def get_rand_list(self, sz: int):
        # for simplicity we are not going to use sz for creationg of the list
        # however, it is possible to do something like this:
        # lst = sz * [None]
        # and don't forget to update the method inside the loop
        lst = []
        for i in range(sz):
            lst.append(random.randint(-self.MAX_RAND_NUM, self.MAX_RAND_NUM))
        random.shuffle(lst)
        return lst


if __name__ == "__main__":
    unittest.main()
