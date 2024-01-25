"""
Suffix Array Slow Constructor

simple, naive and brute force way to build SA
O(n^2log(n))

Inspired by William Fiset
https://github.com/williamfiset/
"""
from suffix_array import SuffixArray


class SuffixArraySlow(SuffixArray):
    class Suffix:
        index, l = 0, 0
        text = []

        def __init__(self, text, index):
            self.l = len(text) - index
            self.index = index
            self.text = text

        # magic fn = less than, important for custom sorting
        def __lt__(self, other):
            if self is other:
                return False
            min_len = min(self.l, other.l)
            for i in range(min_len):
                if self.text[self.index + i] < other.text[other.index + i]:
                    return True
                elif self.text[self.index + i] > other.text[other.index + i]:
                    return False
            return self.l < other.l

        def __str__(self):
            return f"{self.text, self.index, self.l}"

    def __init__(self, text):
        # if text is str => convert it to int[], because T is int[]
        if isinstance(text, str):
            text = self.to_int_array(text)
        super().__init__(text)

    # sorting O(nlog(n)) + string comparison O(n)
    def construct(self):
        self.sa = self.N * [0]
        suffixes = self.N * [None]

        for i in range(self.N):
            suffixes[i] = self.Suffix(self.T, i)

        suffixes.sort()

        for i in range(self.N):
            suffix = suffixes[i]
            self.sa[i] = suffix.index
            suffixes[i] = None

        suffixes = None


sa = SuffixArraySlow("camel")
print(sa)
sa = SuffixArraySlow("AZAZA")
print(sa)
sa = SuffixArraySlow(text="ABABBAB")
print(sa)
