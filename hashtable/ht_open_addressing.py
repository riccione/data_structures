"""
HashTable Open Addressing: base 

Inspired by William Fiset
https://github.com/williamfiset/
"""
import math
from abc import ABC, abstractmethod


class HashTableOpenAddressing(ABC):
    load_factor = None
    capacity = None
    threshold = 0
    modification_count = 0

    used_buckets = 0
    key_count = 0

    keys = []
    value = []

    # marker token for deletion k-v
    # it should be an unique object, in this case we can mark deleted elements
    # with it and during get_value operations do not return None
    TOMBSTONE = object()

    def __init__(self, capacity=7, load_factor=0.65):
        if capacity is None or capacity <= 0:
            raise ValueError(f"Illegal capacity: {capacity}")
        if load_factor is None or load_factor <= 0 or math.isinf(load_factor):
            raise ValueError(f"Illegal load_factor: {load_factor}")
        self.capacity = capacity
        self.load_factor = load_factor
        self.adjust_capacity()
        self.threshold = int(self.capacity * self.load_factor)
        self.keys = self.capacity * [None]
        self.values = self.capacity * [None]

    @abstractmethod
    def setup_probing(self, key):
        pass

    @abstractmethod
    def probe(self, x) -> int:
        pass

    @abstractmethod
    def adjust_capacity(self):
        pass

    def increase_capacity(self):
        self.capacity = 2 * self.capacity + 1

    def clear(self):
        for i in range(self.capacity):
            self.keys[i] = None
            self.values[i] = None
        self.key_count = self.used_buckets = 0
        self.modification_count += 1

    def size(self) -> int:
        return self.key_count

    def get_capacity(self) -> int:
        return self.capacity

    def is_empty(self) -> bool:
        return self.key_count == 0

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def contains(self, key):
        return self.has_key(key)

    # returns list of keys
    def keys(self):
        ht = []
        for i in range(self.capacity):
            if keys[i] is not None and keys[i] != self.TOMBSTONE:
                ht.append(keys[i])
        return ht

    # return list of values
    def values(self):
        ht = []
        for i in range(self.capacity):
            if keys[i] is not None and keys[i] != self.TOMBSTONE:
                ht.append(values[i])
        return ht

    # double size of the hashtable
    def resize_table(self):
        self.increase_capacity()
        self.adjust_capacity()

        self.threshold = int(self.capacity * self.load_factor)

        old_key_table = self.capacity * [None]
        old_value_table = self.capacity * [None]

        # key table pointer swap
        key_table_tmp = self.keys
        self.keys = old_key_table
        old_key_table = key_table_tmp

        # value table pointer swap
        value_table_tmp = self.values
        self.values = old_value_table
        old_value_table = value_table_tmp

        # reset key count and buckets used
        # re-insert all keys into the hashtable
        self.key_count = self.used_buckets = 0

        for i in range(len(old_key_table)):
            if old_key_table[i] is not None and old_key_table[i] != self.TOMBSTONE:
                self.insert(old_key_table[i], old_value_table[i])
            old_value_table[i] = None
            old_key_table[i] = None

    def normalize_index(self, key_hash) -> int:
        return abs(key_hash) % self.capacity

    def gcd(self, a, b) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def insert(self, k, v):
        if k is None:
            raise ValueError("None key")

        if self.used_buckets >= self.threshold:
            self.resize_table()

        self.setup_probing(k)
        offset = self.normalize_index(hash(k))
        j = -1
        x = 1
        i = offset
        while True:
            # current slot was previously deleted
            if self.keys[i] is not None and self.keys[i] == self.TOMBSTONE:
                if j == -1:
                    j = i
            elif self.keys[i] is not None:
                # key already exists in the hashtable, so update its value
                if self.keys[i] == k:
                    old_value = self.values[i]
                    if j == -1:
                        self.values[i] = v
                    else:
                        self.keys[i] = self.TOMBSTONE
                        self.values[i] = None
                        self.keys[j] = k
                        self.values[j] = v
                    self.modification_count += 1
                    return v  # old_value
            else:  # current cell is None, insertion can occur
                # no previously encountered deleted buckets
                if j == -1:
                    self.used_buckets += 1
                    self.key_count += 1
                    self.keys[i] = k
                    self.values[i] = v
                    return v
                # previously seen deleted bucket
                else:
                    self.key_count += 1
                    self.keys[i] = k
                    self.values[i] = v
                self.modification_count += 1
                return None

            i = self.normalize_index(offset + self.probe(x))
            x += 1

    def has_key(self, k) -> bool:
        if k is None:
            raise ValueError("None key")

        self.setup_probing(k)
        offset = self.normalize_index(hash(k))

        j = -1
        x = 1
        i = offset
        while True:
            if self.keys[i] is not None and self.keys[i] == self.TOMBSTONE:
                if j == -1:
                    j = i
            elif self.keys[i] is not None:
                if self.keys[i] == k:
                    # if j != -1 => we previously encountered a deleted cell
                    # we can do an optimization by swapping the entries in cells
                    # i and j so that the next time we search for this key it
                    # will be found faster. This is called lazy
                    # deletion/relocation
                    if j != -1:
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = self.TOMBSTONE
                        self.values[i] = None
                    return True
            else:  # key was not found
                return False
            i = self.normalize_index(offset + self.probe(x))
            x += 1

    # returns None if value is None or key does not exist
    def get(self, k):
        if k is None:
            raise ValueError("None key")

        self.setup_probing(k)
        offset = self.normalize_index(hash(k))

        j = -1
        x = 1
        i = offset
        while True:
            if self.keys[i] is not None and self.keys[i] == self.TOMBSTONE:
                if j == -1:
                    j = i
            elif self.keys[i] is not None:
                if self.keys[i] == k:
                    if j != -1:
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = self.TOMBSTONE
                        self.values[i] = None
                        return self.values[j]
                    else:
                        return self.values[i]
            else:
                return None
            i = self.normalize_index(offset + self.probe(x))
            x += 1

    def remove(self, k):
        if k is None:
            raise ValueError("None key")

        self.setup_probing(k)
        offset = self.normalize_index(hash(k))
        j = -1
        x = 0
        i = offset - 1
        while True:
            i = self.normalize_index(offset + self.probe(x))
            x += 1

            if self.keys[i] is None or self.keys[i] == self.TOMBSTONE:
                continue

            if self.keys[i] is None:
                return None

            if self.keys[i] == k:
                self.key_count -= 1
                self.modification_count += 1
                old_value = self.values[i]
                self.keys[i] = self.TOMBSTONE
                self.values[i] = None
                return old_value

    def __str__(self):
        s = "{ "
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys[i] != self.TOMBSTONE:
                s += f"{self.keys[i]} => {self.values[i]}, "
        s += "}"
        return s

    def __repr__(self):
        s = "{"
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys[i] != self.TOMBSTONE:
                s += f"{self.keys[i]}: {self.values[i]}"
        s += "}"
        return s

    curr = None
    end = None

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        while self.curr < self.capacity:
            x = self.keys[self.curr]
            self.curr += 1
            if x is not None and x != self.TOMBSTONE:
                return x
        raise StopIteration
