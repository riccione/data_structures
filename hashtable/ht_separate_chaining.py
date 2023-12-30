"""
HashTable Separate Chaining

Inspired by William Fiset
https://github.com/williamfiset/

Separate chaining is hash collision resolution technique.
It maintains a DS (linked list, array, balanced tree etc) to hold all the
different values which hashed to a particular value.
"""


class Entry:
    chash = None
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.chash = hash(key)

    def hash_equals(self, entry, other) -> bool:
        return self.chash == other.chash

    # override __str__
    def __str__(self):
        return f"Key=>value: {self.key} => {self.value}"

    def __repr__(self):
        return f"{self.key} => {self.value}"


class HashTableSeparateChaining:
    max_load_factor = 0.0
    capacity = 0
    threshold = 0
    sz = 0

    # instead of using linked list, I use a list due to simplicity in python
    table = []

    # not necessary to define DEFAULT_CAPACITY and DEFAULT_LOAD_FACTOR
    # I use them as optional values in the constructor
    def __init__(self, capacity=3, max_load_factor=0.75):
        if capacity < 0 or capacity is None:
            raise ValueError("Capacity must be > 0 and not None")
        if max_load_factor <= 0 or max_load_factor is None:
            raise ValueError("Max load factor must be > 0 and not None")
        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.threshold = int(self.capacity * self.max_load_factor)
        self.table = self.capacity * [None]

    def size(self) -> int:
        return self.sz

    def is_empty(self) -> bool:
        return self.sz == 0

    # converts a hash value to an index
    def normalize_index(self, key_hash: int) -> int:
        return abs(key_hash) % self.capacity

    def clear(self):
        self.table = [[None] for x in self.table]

    def contains_key(self, key) -> bool:
        return self.has_key(key)

    def has_key(self, key) -> bool:
        bucket_index = self.normalize_index(hash(key))
        return self.bucket_seek_entry(bucket_index, key) is not None

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key is None:
            raise ValueError("Key is None")
        entry = Entry(key, value)
        bucket_index = self.normalize_index(entry.chash)
        return self.bucket_insert_entry(bucket_index, entry)

    def get(self, key):
        if key is None:
            return None
        bucket_index = self.normalize_index(hash(key))
        entry = self.bucket_seek_entry(bucket_index, key)
        if entry is not None:
            return entry.value
        return None

    def remove(self, key):
        if key is None:
            return None
        bucket_index = self.normalize_index(hash(key))
        return self.bucket_remove_entry(bucket_index, key)

    def bucket_remove_entry(self, bucket_index, key):
        entry = self.bucket_seek_entry(bucket_index, key)
        if entry is not None:
            links = self.table[bucket_index]
            links.remove(entry)
            self.sz -= 1
            return entry.value
        else:
            return None

    def bucket_insert_entry(self, bucket_index, entry):
        bucket = self.table[bucket_index]
        if bucket is None:
            bucket = []
            self.table[bucket_index] = bucket

        existent_entry = self.bucket_seek_entry(bucket_index, entry.key)
        if existent_entry is None:
            bucket.append(entry)
            self.sz += 1
            if self.sz > self.threshold:
                self.resize_table()
            return None
        else:
            old_val = existent_entry.value
            existent_entry.value = entry.value
            return old_val

    def bucket_seek_entry(self, bucket_index, key):
        if key is None:
            return None
        bucket = self.table[bucket_index]
        if bucket is None:
            return None
        for e in bucket:
            if e is not None and e.key == key:
                return e
        return None

    def resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.max_load_factor)
        new_table = self.capacity * [None]

        for i in range(len(self.table)):
            if self.table[i] is not None:
                for e in self.table[i]:
                    if e is not None:
                        bucket_index = self.normalize_index(e.chash)
                        bucket = new_table[bucket_index]
                        if bucket is None:
                            bucket = []
                            new_table[bucket_index] = bucket
                            bucket.append(e)

                    # not necessary step in python
                    self.table[i] = None
        self.table = new_table

    def keys(self):
        list_keys = []
        for bucket in self.table:
            if bucket is not None:
                for e in bucket:
                    list_keys.append(e.key)
        return list_keys

    def values(self):
        list_values = []
        for bucket in self.table:
            if bucket is not None:
                for e in bucket:
                    list_values.append(e.value)
        return list_values

    # generator
    def hash_iterator(self):
        if self.sz < 1:
            return None
        for i in range(self.sz):
            if self.table[i] is not None:
                continue
            for e in self.table[i]:
                yield e

    def __str__(self):
        r = ""
        for i in range(self.capacity):
            if self.table[i] is None:
                continue
            for e in self.table[i]:
                r += f"{e}, "
        return r


ht = HashTableSeparateChaining()
ht.add(1, 1)
print(ht.sz)
print(ht.capacity)
print(ht.table)
print(ht)
print(ht.get(1))
ht.add(1, 5)
ht.add(0, 101)
ht.add(4, 2)
# for k in range(25):
#    ht.add(k, k)
print(ht.table)
print("ht.get(4): ", ht.get(4))
ht.remove(4)
print(ht.table)
ht.remove(0)
print(ht.table)
ht.add(0, 201)
ht.put(11, 99)
print(ht.table)
arr = []
for i in range(9):
    random_val = 17
    arr.append(random_val)
    ht.put(i, random_val)
    print(i, ht.table)

ht.clear()
print(ht.table)
