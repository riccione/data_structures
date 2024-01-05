"""
HashTable Open Addressing: Quadratic Probing

Inspired by William Fiset
https://github.com/williamfiset/
"""
from ht_open_addressing import HashTableOpenAddressing


class HashTableQuadraticProbing(HashTableOpenAddressing):
    # const for linear probing
    LINEAR_CONSTANT = 17

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def next_power_of_two(self, n: int) -> int:
        if n == 0:
            return 0
        # finding highest one bit in parenthesis
        return (1 << (n.bit_length() - 1)) << 1

    def setup_probing(self, k):
        pass

    def probe(self, x) -> int:
        return (x * x + x) >> 1

    def increase_capacity(self):
        self.capacity = self.next_power_of_two(self.capacity)

    def adjust_capacity(self):
        pow2 = 1 << (self.capacity.bit_length() - 1)
        if self.capacity == pow2:
            return
        self.increase_capacity()


"""
ht = HashTableQuadraticProbing()
ht.put(-1, 5)
ht.put(2, 5)
print(ht)
ht.remove(-1)
ht.remove(2)
print(ht)
ran = []
for i in range(-5, 5):
    ran.append(i)
for k in ran:
    ht.add(k, k)

print(ht)
print(ht.capacity)
print(ht.key_count)
ans = []
for k in ht:
    ans.append(k)
print(ans)
"""
