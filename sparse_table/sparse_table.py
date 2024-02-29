"""
Sparse Table

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""
from enum import Enum
import math

# Operation = Enum('Operation', ['MIN', 'MAX', 'SUM', 'MULT', 'GCD'])


class Operation(Enum):
    MIN = min
    MAX = max
    SUM = sum
    MULT = lambda a, b: a * b
    GCD = math.gcd


class SparseTable:
    def __init__(self, values, op):
        # len of original input list
        self.n = len(values)
        # max power of 2, floor(log2(n))
        self.P = 0
        # fast log base 2 log lookup table for i, 1 <= i <= n
        self.log2 = []
        # sparse table values
        self.dp = [[]]
        # index table associated with values in the sparse table
        self.it = [[]]

        self.op = op
        self.init(values)

    def init(self, v):
        self.n = len(v)

        self.P = int(math.log2(self.n))
        self.dp = [[0] * self.n for _ in range(self.P + 1)]
        self.it = [[0] * self.n for _ in range(self.P + 1)]

        for i in range(self.n):
            self.dp[0][i] = v[i]
            self.it[0][i] = i

        self.log2 = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log2[i] = self.log2[i // 2] + 1

        # build sparse table combining values of the previous intervals
        for i in range(1, self.P + 1):
            j = 0
            while (j + (1 << i)) <= self.n:
                left_interval = self.dp[i - 1][j]
                right_interval = self.dp[i - 1][j + (1 << (i - 1))]
                if self.op == Operation.MIN:
                    self.dp[i][j] = min(left_interval, right_interval)
                    if left_interval <= right_interval:
                        self.it[i][j] = self.it[i - 1][j]
                    else:
                        self.it[i][j] = self.it[i - 1][j + (1 << (i - 1))]
                elif self.op == Operation.MAX:
                    self.dp[i][j] = max(left_interval, right_interval)
                    if left_interval >= right_interval:
                        self.it[i][j] = self.it[i - 1][j]
                    else:
                        self.it[i][j] = self.it[i - 1][j + (1 << (i - 1))]
                elif self.op == Operation.SUM:
                    self.dp[i][j] = left_interval + right_interval
                elif self.op == Operation.MULT:
                    self.dp[i][j] = left_interval * right_interval
                else:  # GCD
                    self.dp[i][j] = math.gcd(left_interval, right_interval)
                j += 1

        # for debugging
        # print(self.dp)

    def __str__(self):
        ind = ""
        s = ""
        for xs in self.dp:
            tmp = ""
            for i, x in enumerate(xs):
                tmp += "{:<4}".format(i)
                s += "{:<4}".format(x)
            ind = tmp + "\n"
            s += "\n"
        return ind + s

    def query_index(self, l: int, r: int):
        # fast queries O(1)
        if self.op in [Operation.MIN, Operation.MAX, Operation.GCD]:
            return self._query_index_fast(l, r)
        else:  # slower queries O(log2(n))
            return self._query_index_slower(l, r)

    def _query_index_fast(self, l, r):
        length = r - l + 1
        p = self.log2[length]
        left_interval = self.dp[p][l]
        right_interval = self.dp[p][r - (1 << p) + 1]
        if self.op == Operation.MIN:
            if left_interval <= right_interval:
                return self.it[p][l]
            else:
                return self.it[p][r - (1 << p) + 1]
        elif self.op == Operation.MAX:
            if left_interval >= right_interval:
                return self.it[p][l]
            else:
                return self.it[p][r - (1 << p) + 1]

    def _query_index_slower(self, l, r):
        r = 0
        if self.op == Operation.MULT:
            r = 1
        p = self.log2[r - l + 1]
        while l < r:
            if self.op == Operation.MULT:
                mult *= self.dp[p][l]
            else:  # SUM case
                sum += self.dp[p][l]
            p = int(self.log2[r - l + 1])
            l += 1 << p
        return r

    def query_value(self, l, r):
        if self.op in [Operation.MIN, Operation.MAX, Operation.GCD]:
            len_ = r - l + 1
            p = self.log2[len_]
            return self.op.value(self.dp[p][l], self.dp[p][r - (1 << p) + 1])
        else:
            # MULT, SUM
            if self.op == Operation.MULT:
                m = 1
                p = self.log2[r - l + 1]
                while l <= r:
                    m *= self.dp[p][l]
                    l += 1 << p
                    p = self.log2[r - l + 1]
                return m
            else:
                sum_ = 0
                p = self.log2[r - l + 1]
                while l <= r:
                    sum_ += self.dp[p][l]
                    l += 1 << p
                    p = self.log2[r - l + 1]
                return sum_


values = [1, 0, 1, -2, 3, -4, 5, -6, 7, -8, 9]
# values = [4,2,3,7,1,5,3,3,9,6,7,-1,4]
st = SparseTable(values, Operation.MIN)
print(st)
print("Len: ", len(values))
print("Index is: ", st.query_index(0, 1))
print("Value is: ", st.query_value(0, 1))
print("Index is: ", st.query_index(0, len(values) - 1))
print("Value is: ", st.query_value(0, len(values) - 1))
st = SparseTable(values, Operation.MAX)
print(st)
print("Len: ", len(values))
print("Index is: ", st.query_index(0, 1))
print("Value is: ", st.query_value(0, 1))
print("Index is: ", st.query_index(0, len(values) - 1))
print("Value is: ", st.query_value(0, len(values) - 1))
