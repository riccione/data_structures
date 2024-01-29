"""
Suffix Array Fast Constructor
O(nlog(n))

Inspired by William Fiset
https://github.com/williamfiset/
"""
from suffix_array import SuffixArray


class SuffixArrayFast(SuffixArray):
    DEFAULT_ALPHABET_SIZE = 256
    alphabet_size = 0
    sa2 = []
    rank = []
    tmp = []
    c = []

    def __init__(self, text, alphabet_size=DEFAULT_ALPHABET_SIZE):
        self.alphabet_size = alphabet_size
        # if text is str => convert it to int[], because T is int[]
        if isinstance(text, str):
            text = self.to_int_array(text)
        super().__init__(text)

    def construct(self):
        self.sa = [0] * self.N
        sa2 = [0] * self.N
        rank = [0] * self.N
        c = [0] * max(self.alphabet_size, self.N)

        for i in range(self.N):
            rank[i] = self.T[i]
            c[rank[i]] += 1

        for i in range(1, self.alphabet_size):
            c[i] += c[i - 1]

        i = self.N - 1
        while i >= 0:
            ind = self.T[i]
            c[ind] -= 1
            self.sa[c[ind]] = i
            i -= 1

        p = 1
        while p < self.N:
            r = 0
            for i in range(self.N - p, self.N):
                sa2[r] = i
                r += 1

            for i in range(self.N):
                if self.sa[i] >= p:
                    sa2[r] = self.sa[i] - p
                    r += 1

            # reset c to int filled with 0
            c = [0] * self.alphabet_size

            for i in range(self.N):
                c[rank[i]] += 1

            for i in range(1, self.alphabet_size):
                c[i] += c[i - 1]

            for i in range(self.N - 1, -1, -1):
                c[rank[sa2[i]]] -= 1
                self.sa[c[rank[sa2[i]]]] = sa2[i]

            r = sa2[self.sa[0]] = 0

            for i in range(1, self.N):
                if not (
                    rank[self.sa[i - 1] == rank[self.sa[i]]]
                    and self.sa[i - 1] + p < self.N
                    and self.sa[i] + p < self.N
                    and rank[self.sa[i - 1] + p] == rank[self.sa[i] + p]
                ):
                    r += 1
                sa2[self.sa[i]] = r

            tmp = rank
            rank = sa2
            sa2 = tmp
            if r == self.N - 1:
                break
            self.alphabet_size = r + 1
            p <<= 1


"""
sa = SuffixArrayFast(text="camel")
print(sa)
sa = SuffixArrayFast(text="AZAZA")
print(sa)
sa = SuffixArrayFast(text="ABABBAB")
print(sa)
"""
print(SuffixArrayFast(text="B0AB2A3"))
