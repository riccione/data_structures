"""
HashTable Open Addressing: Linear Probing

Inspired by William Fiset
https://github.com/williamfiset/
"""
from ht_open_addressing import HashTableOpenAddressing


class HashTableLinearProbing(HashTableOpenAddressing):
    # const for linear probing
    LINEAR_CONSTANT = 17

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup_probing(self, k):
        pass

    def probe(self, x) -> int:
        return self.LINEAR_CONSTANT * x

    def adjust_capacity(self):
        while super().gcd(self.LINEAR_CONSTANT, super().get_capacity()) != 1:
            self.capacity += 1


"""
ht = HashTableLinearProbing()
ht.put(-1, 5)
ht.put(2, 5)
ht.remove(-1)
ht.remove(2)
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
