"""
Indexed Priority Queue

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""


class MinIndexedDHeap:
    def __init__(self, degree: int, max_size: int):
        if max_size <= 0:
            raise ValueError("max_size <= 0")

        # degree of every node in the heap
        self.D = max(2, degree)

        # max number of elements in the heap
        self.N = max(self.D + 1, max_size)

        # inverse map = stores indexes of the keys in the range (0, sz] which
        # make up the PQ. im is inverse of pm, so pm[im[i]] = im[pm[i]] = i
        self.im = [-1] * self.N

        # position map maps Key Indexes (ki)
        self.pm = [-1] * self.N

        # lookup arrays to track the child/parent indexes of each node
        self.child = [0] * self.N
        self.parent = [0] * self.N

        # values associated with the key. This array is indexed by the key
        # indexes (ki)
        # in python it is not necessary to make each el as an Object
        self.values = [None] * self.N

        # current number of elements in the heap
        self.sz = 0

        for i in range(self.N):
            self.parent[i] = (i - 1) // self.D
            self.child[i] = i * self.D + 1

    def size(self) -> int:
        return self.sz

    def is_empty(self) -> bool:
        return self.sz == 0

    def contains(self, ki: int) -> bool:
        self.key_in_bounds_or_throw(ki)
        return self.pm[ki] != -1

    def peek_min_key_index(self) -> int:
        self.is_not_empty_or_throw()
        return self.im[0]

    def poll_min_key_index(self):
        min_ki = self.peek_min_key_index()
        self.delete(min_ki)
        return min_ki

    def peek_min_value(self):
        self.is_not_empty_or_throw()
        return self.values[self.im[0]]

    def poll_min_value(self):
        min_value = self.peek_min_value()
        self.delete(self.peek_min_key_index())
        return min_value

    def insert(self, ki: int, value):
        if self.contains(ki):
            raise ValueError(f"Index already exists; received {ki}")
        self.value_not_null_or_throw(value)

        self.pm[ki] = self.sz
        self.im[self.sz] = ki
        self.values[ki] = value
        self.swim(self.sz)
        self.sz += 1

    def value_of(self, ki: int):
        self.key_exists_or_throw(ki)
        return self.values[ki]

    def delete(self, ki: int):
        self.key_exists_or_throw(ki)
        i = self.pm[ki]
        self.swap(i, self.sz - 1)
        self.sz -= 1
        self.sink(i)
        self.swim(i)
        value = self.values[ki]
        self.values[ki] = None
        self.pm[ki] = -1
        self.im[self.sz] = -1
        return value

    def update(self, ki: int, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        i = self.pm[ki]
        old_value = self.values[ki]
        self.values[ki] = value
        self.sink(i)
        self.swim(i)
        return old_value

    def decrease(self, ki: int, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        if value < self.values[ki]:
            self.values[ki] = value
            self.swim(self.pm[ki])

    def increase(self, ki: int, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        if self.values[ki] < value:
            self.values[ki] = value
            self.sink(self.pm[ki])

    # helper fn
    def sink(self, i: int):
        j = self.min_child(i)
        while j != -1:
            self.swap(i, j)
            i = j
            j = self.min_child(i)

    def swim(self, i: int):
        while i > 0 and self.less(i, self.parent[i]):
            self.swap(i, self.parent[i])
            i = self.parent[i]

    def min_child(self, i: int) -> int:
        index = -1
        start = self.child[i]
        end = min(self.sz, start + self.D)
        j = start
        for j in range(start, end):
            if self.less(j, i):
                index = i = j
        return index

    def swap(self, i: int, j: int):
        self.pm[self.im[j]] = i
        self.pm[self.im[i]] = j
        self.im[i], self.im[j] = self.im[j], self.im[i]

    def less(self, i: int, j: int) -> bool:
        v1 = self.values[self.im[i]]
        v2 = self.values[self.im[j]]
        if v1 and v2:
            return v1 < v2
        return i < j

    def __str__(self):
        return " ".join(str(x) for x in self.im)

    # helper fn
    def is_not_empty_or_throw(self):
        if self.is_empty():
            raise ValueError("Priority queue underflow")

    def key_exists_and_value_not_null_or_throw(self, ki: int, value):
        self.key_exists_or_throw(ki)
        self.value_not_null_or_throw(value)

    def key_exists_or_throw(self, ki: int):
        if not self.contains(ki):
            raise ValueError(f"Index does not exist; {ki}")

    def value_not_null_or_throw(self, value):
        if value is None:
            raise ValueError("value cannot be None")

    def key_in_bounds_or_throw(self, ki: int):
        if ki < 0 or ki >= self.N:
            raise ValueError(f"Key index out of bounds; {ki}")

    # test fn
    def is_min_heap(self) -> bool:
        return _is_min_heap(0)

    def _is_min_heap(self, i: int) -> bool:
        from_ = self.child[i]
        to_ = min(self.sz, from_ + self.D)
        j = from_
        while j < to_:
            if not self.less(i, j):
                return False
            if not self._is_min_heap(j):
                return False
            j += 1

        return True
