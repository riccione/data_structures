"""
Union Find

Inspired by William Fiset
https://github.com/williamfiset/

2 operations only:
- find
- unify
"""


class UnionFind:
    # number of elements in the union find
    sz = 0
    # size of each of the component
    size_component = []
    # id[i] points to the parent of i, if id[i] == i then i is a root node
    # root is always points to itself
    id_parent = []

    # number of components in the union find
    num_components = 0

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")

        self.sz = self.num_components = size

        # size_component and id do not require size due to dynamic nature of
        # arrays in python
        self.size_component = self.sz * [None]
        self.id_parent = self.sz * [None]

        for i in range(size):
            self.id_parent[i] = i  # link to itself (self root)
            # each component is originally of size one
            self.size_component[i] = 1

    def find(self, p: int) -> int:
        # find the root of the component/set
        root = p
        while root != self.id_parent[root]:
            root = self.id_parent[root]

        # do path compression, it gives us amortized time complexity
        while p != root:
            next_ = self.id_parent[p]
            self.id_parent[p] = root
            p = next_

        return root

    # alternative method using recursion
    def find_alt(self, p: int) -> int:
        if p == self.id_parent[p]:
            return p
        self.id_parent[p] = self.find_alt(self.id_parent[p])
        return self.id_parent[p]

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def component_size(self, p: int) -> int:
        return self.size_component[self.find(p)]

    def size(self) -> int:
        return self.sz

    def components(self) -> int:
        return self.num_components

    def unify(self, p: int, q: int):
        if self.connected(p, q):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        # merge smaller component/set into the larget one
        if self.size_component[root1] < self.size_component[root2]:
            self.size_component[root2] += self.size_component[root1]
            self.id_parent[root1] = root2
            self.size_component[root1] = 0
        else:
            self.size_component[root1] += self.size_component[root2]
            self.id_parent[root2] = root1
            self.size_component[root2] = 0

        self.num_components -= 1


uf = UnionFind(5)
print(uf.components())
uf.unify(0, 1)
print(uf.components())
print(uf.size())
