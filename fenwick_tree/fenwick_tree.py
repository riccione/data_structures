"""
Fenwick Tree = Binary Indexed Tree

Inspired by William Fiset
https://github.com/williamfiset/
"""
import copy


class FenwickTree:
    N = 0
    tree = []

    def __init__(self, sz=1, values=None):
        if values is None:
            if sz is None:
                raise ValueError("Size cannot be None")
            self.N = sz + 1
            self.tree = self.N * [0]
        else:
            # copies values and all its content
            # this is unnecessary with Python
            self.tree = copy.deepcopy(values)
            self.N = len(self.tree)
            for i in range(1, len(self.tree)):
                j = i + self.lsb(i)
                if j < self.N:
                    self.tree[j] += self.tree[i]

    def lsb(self, i: int) -> int:
        # isolate the lowest one bit value
        return i & -i

    # count sum from [1, i], one based, O(log(n))
    def prefix_sum(self, i: int) -> int:
        r = 0
        while i != 0:
            r += self.tree[i]
            i = i & ~self.lsb(i)  # or i -= lsb(i)
        return r

    # count sum from [i, j], one based, O(log(n))
    def sum_(self, l: int, r: int) -> int:
        if r < l:
            raise ValueError("r should be >= l")
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    def get(self, i: int) -> int:
        return sum_(i, i)

    # add k to index i, one based, O(log(n))
    def add(self, i: int, k: int):
        while i < self.N:
            self.tree[i] += k
            i += self.lsb(i)

    # set index i to be equal to k, one based, O(log(n))
    def set_(self, i, k):
        value = self.sum_(i, i)
        self.add(i, k - value)

    def __str__(self):
        return f"{self.tree}"

    def __repr__(self):
        return f"{self.tree}"


# ft = FenwickTree(sz=10)
# print(ft)
# ft.set_(1, 12)
# print(ft)
