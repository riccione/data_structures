"""
Tests for Suffix Array implementation

Inspired by William Fiset
https://github.com/williamfiset/

"""
import random
import unittest
from suffix_array_slow import SuffixArraySlow
from suffix_array_med import SuffixArrayMed
from suffix_array_fast import SuffixArrayFast


class TestSA(unittest.TestCase):
    LOOPS = 1000
    TEST_SZ = 40
    NUM_NULLS = TEST_SZ / 5
    MAX_RAND_NUM = 250

    ASCII_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def test_sa_length(self):
        s = "ABCDE"
        sa1 = SuffixArraySlow(s)
        sa2 = SuffixArrayMed(s)
        sa3 = SuffixArrayFast(s)

        self.assertEqual(len(sa1.get_sa()), len(s))
        self.assertEqual(len(sa2.get_sa()), len(s))
        self.assertEqual(len(sa3.get_sa()), len(s))

    def test_lcs_unique_chars(self):
        sa1 = SuffixArraySlow(self.ASCII_LETTERS)
        sa2 = SuffixArrayMed(self.ASCII_LETTERS)
        sa3 = SuffixArrayFast(self.ASCII_LETTERS)

        sas = [sa1, sa2, sa3]

        for x in sas:
            for i in range(len(x.get_sa())):
                self.assertEqual(x.get_lcp_array()[i], 0)

    def test_increasing_lcp(self):
        unique_chars = "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
        sa1 = SuffixArraySlow(unique_chars)
        sa2 = SuffixArrayMed(unique_chars)
        sa3 = SuffixArrayFast(unique_chars)

        sas = [sa1, sa2, sa3]

        for x in sas:
            for i in range(len(x.get_sa())):
                self.assertEqual(x.get_lcp_array()[i], i)

    def test_lcp1(self):
        s = "ABBABAABAA"
        lcp_values = [0, 1, 2, 1, 4, 2, 0, 3, 2, 1]

        sa1 = SuffixArraySlow(s)
        sa2 = SuffixArrayMed(s)
        sa3 = SuffixArrayFast(s)

        sas = [sa1, sa2, sa3]

        for x in sas:
            for i in range(len(x.get_sa())):
                self.assertEqual(lcp_values[i], x.get_lcp_array()[i])

    def test_lcp2(self):
        s = "ABABABAABB"
        lcp_values = [0, 1, 3, 5, 2, 0, 1, 2, 4, 1]

        sa1 = SuffixArraySlow(s)
        sa2 = SuffixArrayMed(s)
        sa3 = SuffixArrayFast(s)

        sas = [sa1, sa2, sa3]

        for x in sas:
            for i in range(len(x.get_sa())):
                self.assertEqual(lcp_values[i], x.get_lcp_array()[i])

    def test_sa_construction(self):
        # use digits 0-9 to fake unique tokens
        s = "BAAAAB0ABAAAAB1BABA2ABA3AAB4BBBB5BB"
        # TODO: fast algorithm has a bug and does not create SA correctly
        # s = "B0AB2A3"

        sa1 = SuffixArraySlow(s)
        sa2 = SuffixArrayMed(s)
        sa3 = SuffixArrayFast(s)

        sas = [sa1, sa2]  # , sa3]

        # print(sa1)
        # print(sa2)
        # print(sa3)

        for i in range(len(sas)):
            for j in range(i + 1, len(sas)):
                s1 = sas[i]
                s2 = sas[j]
                for k in range(len(s1.get_sa())):
                    self.assertEqual(s1.get_sa()[k], s2.get_sa()[k])


if __name__ == "__main__":
    unittest.main()
