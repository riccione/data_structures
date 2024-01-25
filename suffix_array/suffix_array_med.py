"""
Suffix Array Medium Constructor
O(nlog^2(n))

Inspired by William Fiset
https://github.com/williamfiset/
"""
from suffix_array import SuffixArray


class SuffixArrayMed(SuffixArray):
    class SuffixRankTuple:
        first_half = 0
        second_half = 0
        original_index = 0

        def __init__(self, fh=0, sh=0, oi=0):
            self.first_half = fh
            self.second_half = sh
            self.original_index = oi

        # magic fn = less than, important for custom sorting
        def __lt__(self, other):
            if self.first_half != other.first_half:
                return self.first_half < other.first_half
            return self.second_half < other.second_half

        def __str__(self):
            return f"{self.original_index} -> {self.first_half, self.second_half}"

        def __repr__(self):
            return f"({self.original_index},{self.first_half},{self.second_half})"

    def __init__(self, text):
        if isinstance(text, str):
            text = self.to_int_array(text)
        super().__init__(text)

    def construct(self):
        self.sa = self.N * [0]

        # maintain suffix rank in both a matrix with two rows containing the
        # current and last rank information as well as some sortable rank
        # objects
        suffix_ranks = [[0] * self.N for i in range(2)]
        ranks = self.N * [self.SuffixRankTuple]

        # assign a numerical value to each character in the text
        for i in range(self.N):
            suffix_ranks[0][i] = self.T[i]
            ranks[i] = self.SuffixRankTuple()

        # O(log(n))
        pos = 1
        while pos < self.N:
            for i in range(self.N):
                sr = ranks[i]
                sr.first_half = suffix_ranks[0][i]
                sr.second_half = suffix_ranks[0][pos + i] if i + pos < self.N else -1
                sr.original_index = i

            # O(nlog(n))
            # breakpoint()
            ranks.sort()
            new_rank = 0
            suffix_ranks[1][ranks[0].original_index] = 0

            for i in range(1, self.N):
                last_s_rank = ranks[i - 1]
                curr_s_rank = ranks[i]

                # if the first half differs from the second half
                if (
                    curr_s_rank.first_half != last_s_rank.first_half
                    or curr_s_rank.second_half != last_s_rank.second_half
                ):
                    new_rank += 1

                suffix_ranks[1][curr_s_rank.original_index] = new_rank

            # place top row (current row) to be the last row
            suffix_ranks[0] = suffix_ranks[1]

            # optimization to stop early
            if new_rank == self.N - 1:
                break

            pos *= 2

        # fill suffix array
        for i in range(self.N):
            self.sa[i] = ranks[i].original_index
            ranks[i] = None

        # cleanup
        suffix_ranks[0] = suffix_ranks[1] = None
        suffix_ranks = None
        ranks = None


sa = SuffixArrayMed("camel")
print(sa)
sa = SuffixArrayMed("AZAZA")
print(sa)
sa = SuffixArrayMed(text="ABABBAB")
print(sa)
