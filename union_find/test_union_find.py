import unittest
from union_find import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_num_components(self):
        uf = UnionFind(5)
        self.assertEqual(uf.components(), 5)
        uf.unify(0, 1)
        self.assertEqual(uf.components(), 4)
        uf.unify(1, 0)
        self.assertEqual(uf.components(), 4)
        uf.unify(1, 2)
        self.assertEqual(uf.components(), 3)
        uf.unify(0, 2)
        self.assertEqual(uf.components(), 3)
        uf.unify(2, 1)
        self.assertEqual(uf.components(), 3)
        uf.unify(3, 4)
        self.assertEqual(uf.components(), 2)
        uf.unify(4, 3)
        self.assertEqual(uf.components(), 2)
        uf.unify(1, 3)
        self.assertEqual(uf.components(), 1)
        uf.unify(4, 0)
        self.assertEqual(uf.components(), 1)

    def test_component_size(self):
        uf = UnionFind(5)
        self.assertEqual(uf.component_size(0), 1)
        self.assertEqual(uf.component_size(1), 1)
        self.assertEqual(uf.component_size(2), 1)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(0, 1)
        self.assertEqual(uf.component_size(0), 2)
        self.assertEqual(uf.component_size(1), 2)
        self.assertEqual(uf.component_size(2), 1)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(1, 0)
        self.assertEqual(uf.component_size(0), 2)
        self.assertEqual(uf.component_size(1), 2)
        self.assertEqual(uf.component_size(2), 1)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(1, 2)
        self.assertEqual(uf.component_size(0), 3)
        self.assertEqual(uf.component_size(1), 3)
        self.assertEqual(uf.component_size(2), 3)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(0, 2)
        self.assertEqual(uf.component_size(0), 3)
        self.assertEqual(uf.component_size(1), 3)
        self.assertEqual(uf.component_size(2), 3)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(2, 1)
        self.assertEqual(uf.component_size(0), 3)
        self.assertEqual(uf.component_size(1), 3)
        self.assertEqual(uf.component_size(2), 3)
        self.assertEqual(uf.component_size(3), 1)
        self.assertEqual(uf.component_size(4), 1)

        uf.unify(3, 4)
        self.assertEqual(uf.component_size(0), 3)
        self.assertEqual(uf.component_size(1), 3)
        self.assertEqual(uf.component_size(2), 3)
        self.assertEqual(uf.component_size(3), 2)
        self.assertEqual(uf.component_size(4), 2)

        uf.unify(4, 3)
        self.assertEqual(uf.component_size(0), 3)
        self.assertEqual(uf.component_size(1), 3)
        self.assertEqual(uf.component_size(2), 3)
        self.assertEqual(uf.component_size(3), 2)
        self.assertEqual(uf.component_size(4), 2)

        uf.unify(1, 3)
        self.assertEqual(uf.component_size(0), 5)
        self.assertEqual(uf.component_size(1), 5)
        self.assertEqual(uf.component_size(2), 5)
        self.assertEqual(uf.component_size(3), 5)
        self.assertEqual(uf.component_size(4), 5)

        uf.unify(4, 0)
        self.assertEqual(uf.component_size(0), 5)
        self.assertEqual(uf.component_size(1), 5)
        self.assertEqual(uf.component_size(2), 5)
        self.assertEqual(uf.component_size(3), 5)
        self.assertEqual(uf.component_size(4), 5)

    def test_connectivity(self):
        x = 7
        uf = UnionFind(x)
        for i in range(x):
            self.assertTrue(uf.connected(i, i))

        uf.unify(0, 2)
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(3, 1))
        self.assertFalse(uf.connected(6, 4))
        self.assertFalse(uf.connected(5, 0))

        uf.unify(3, 1)
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))
        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 1))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(2, 3))
        self.assertFalse(uf.connected(1, 0))
        self.assertFalse(uf.connected(2, 1))
        self.assertFalse(uf.connected(3, 2))

        self.assertFalse(uf.connected(1, 4))
        self.assertFalse(uf.connected(2, 5))
        self.assertFalse(uf.connected(3, 6))

        for i in range(x):
            self.assertTrue(uf.connected(i, i))

        uf.unify(2, 5)
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))
        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 1))
        self.assertTrue(uf.connected(0, 5))
        self.assertTrue(uf.connected(5, 0))
        self.assertTrue(uf.connected(5, 2))
        self.assertTrue(uf.connected(2, 5))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(2, 3))
        self.assertFalse(uf.connected(1, 0))
        self.assertFalse(uf.connected(2, 1))
        self.assertFalse(uf.connected(3, 2))

        self.assertFalse(uf.connected(4, 6))
        self.assertFalse(uf.connected(4, 5))
        self.assertFalse(uf.connected(1, 6))

        for i in range(x):
            self.assertTrue(uf.connected(i, i))

        # connect everything
        uf.unify(1, 2)
        uf.unify(3, 4)
        uf.unify(4, 6)

        for i in range(x):
            for j in range(x):
                self.assertTrue(uf.connected(i, j))

    def test_size(self):
        uf = UnionFind(5)
        self.assertEqual(uf.size(), 5)
        uf.unify(0, 1)
        uf.find(3)
        self.assertEqual(uf.size(), 5)
        uf.unify(1, 2)
        self.assertEqual(uf.size(), 5)
        uf.unify(0, 2)
        uf.find(1)
        self.assertEqual(uf.size(), 5)
        uf.unify(2, 1)
        self.assertEqual(uf.size(), 5)
        uf.unify(3, 4)
        uf.find(0)
        self.assertEqual(uf.size(), 5)
        uf.unify(4, 3)
        uf.find(3)
        self.assertEqual(uf.size(), 5)
        uf.unify(1, 3)
        self.assertEqual(uf.size(), 5)
        uf.find(2)
        uf.unify(4, 0)
        self.assertEqual(uf.size(), 5)

    def test_uf_create(self):
        s = [-1, -3463, 0]
        for x in s:
            with self.assertRaises(ValueError):
                uf = UnionFind(x)


if __name__ == "__main__":
    unittest.main()
