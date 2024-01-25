"""
Suffix Array

Inspired by William Fiset
https://github.com/williamfiset/
"""
from abc import ABC, abstractmethod


class SuffixArray(ABC):
    N = 0  # length of sa

    T = []  # text represented as int array

    sa = []  # sorted sa

    lcp = []  # longest common prefix array

    constructed_sa = False
    constructed_lcp = False

    def __init__(self, text):
        if text is None:
            raise ValueError("Text cannot be None")

        self.T = text
        self.N = len(text)
        self.build_sa()
        self.build_lcp()

    def get_text_length(self):
        return len(self.T)

    def get_sa(self):
        self.build_sa()
        return self.sa

    def get_lcp_array(self):
        self.build_lcp()
        return self.lcp

    def build_sa(self):
        if self.constructed_sa:
            return
        self.construct()
        self.constructed_sa = True

    def build_lcp(self):
        if self.constructed_lcp:
            return
        self.build_sa()
        self.kasai()
        self.constructed_lcp = True

    @abstractmethod
    def construct(self):
        pass

    def to_int_array(self, text: str):
        if text is None:
            return None
        return [ord(x) for x in text]

    # Kasai algorithm to build LCP array, O(n)
    # http://www.mi.fu-berlin.de/wiki/pub/ABI/RnaSeqP4/suffix-array.pdf
    def kasai(self):
        # build suffix array first => self.sa

        # init empty LCP array
        self.lcp = self.N * [0]

        # create inversed suffix array => inv, it helps in finding the position
        # of a suffix in the sorted order quickly
        inv = self.N * [0]
        for i in range(self.N):
            inv[self.sa[i]] = i

        l = 0
        for i in range(self.N):
            if inv[i] > 0:
                k = self.sa[inv[i] - 1]
                while (
                    (i + l) < self.N
                    and (k + l) < self.N
                    and self.T[i + l] == self.T[k + l]
                ):
                    l += 1
                self.lcp[inv[i]] = l
                if l > 0:
                    l -= 1

    def __str__(self):
        if len(self.sa) < 1:
            raise ValueError("suffix array is empty, try to build it first")
        s = "-----i-----SA-----LCP-----Suffix\n"

        for i in range(self.N):
            suffix_len = self.N - self.sa[i]
            suffix_arr = suffix_len * [0]
            k = 0
            for j in range(self.sa[i], self.N):
                suffix_arr[k] = self.T[j]
                k += 1
            # suffix = str(suffix_arr)
            suffix = "".join([chr(x) for x in suffix_arr])
            formatted_str = (
                f"{'-':<5}{i:<6}{self.sa[i]:<7}{self.lcp[i]:<8}{suffix:<8}\n"
            )
            s += formatted_str

        return s
