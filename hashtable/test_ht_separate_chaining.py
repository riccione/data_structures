"""
TODO: implement all tests
"""
import unittest
from ht_separate_chaining import HashTableSeparateChaining
import random


class TestHTSeparateChaining(unittest.TestCase):
    LOOPS = 500
    MAX_SIZE = random.randint(1, 750)
    MAX_RAND_NUM = random.randint(1, 350)

    def test_illegal_creating(self):
        with self.assertRaises(ValueError):
            HashTableSeparateChaining(-3, 0.5)

    def test_illegal_creating2(self):
        with self.assertRaises(ValueError):
            HashTableSeparateChaining(6, -0.5)

    def test_legal_creating3(self):
        try:
            HashTableSeparateChaining(6, 0.9)
        except ValueError:
            self.fail("ValueError")

    def test_update_value(self):
        map1 = HashTableSeparateChaining()
        map1.add(1, 1)
        self.assertEqual(map1.get(1), 1)
        map1.add(1, 5)
        self.assertEqual(map1.get(1), 5)
        map1.add(1, -7)
        self.assertEqual(map1.get(1), -7)

    def test_iterator(self):
        map1 = HashTableSeparateChaining()
        map2 = HashTableSeparateChaining()
        rand_nums = random.randint(1, 700)
        count = 0
        for k in range(rand_nums):
            self.assertEqual(map1.add(k, k), map2.put(k, k))
            count += 1

        for k in map1.hash_iterator():
            self.assertEqual(map1.get(k), k)
            self.assertEqual(map1.get(k), map2.get(k))
            self.assertTrue(map1.has_key(k))
            self.assertTrue(map1.contains_key(k))

        self.assertTrue(map1.size(), count)
        self.assertTrue(map2.size(), count)

    def test_remove(self):
        for i in range(self.LOOPS):
            map1 = HashTableSeparateChaining()
            map1.clear()

            arr = []
            for i in range(self.MAX_SIZE):
                random_val = random.randint(-self.MAX_RAND_NUM, self.MAX_RAND_NUM)
                arr.append(random_val)
                map1.put(i, random_val)

            self.assertEqual(map1.size(), len(arr))

            keys = map1.keys()
            for k in keys:
                map1.remove(k)

            self.assertTrue(map1.is_empty())


if __name__ == "__main__":
    unittest.main()
