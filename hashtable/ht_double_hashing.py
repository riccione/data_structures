"""
HashTable Open Addressing: Double Hashing

Inspired by William Fiset
https://github.com/williamfiset/
"""
from ht_open_addressing import HashTableOpenAddressing


class HashTableDoubleHashing(HashTableOpenAddressing):
    chash = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup_probing(self, k):
        # cache second hash value
        self.chash = self.normalize_index(hash(k))

        # fail safe to avoid infinite loop
        if self.chash == 0:
            self.chash = 1

    def probe(self, x) -> int:
        return x * self.chash

    # adjust until it is a prime number
    def adjust_capacity(self):
        while not self.is_prime(self.capacity):
            self.capacity += 1

    # https://en.wikipedia.org/wiki/List_of_prime_numbers
    # https://en.wikipedia.org/wiki/Primality_test
    def is_prime(self, x: int) -> int:
        if x <= 3 and x > 1:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        # finding sqrt of n
        e = int(x ** (1 / 2))
        for i in range(5, e + 1):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True


"""
ht = HashTableDoubleHashing()
print(ht.is_prime(35))
ht.add(1, 5)
ht.add(2, 5)
ht.add(3, 5)
ht.add(4, 5)
ht.add(5, 5)
#ht.add(6, 5)
#ht.add(7, 5)
#ht.add(8, 5)
print(ht.capacity, ht.size())
#for i in range(8, 100):
#    ht = HashTableDoubleHashing(capacity=i)
#    print(ht.capacity, ht.size())
ht = HashTableDoubleHashing()
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
