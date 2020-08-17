# program for implementing fenwick trees.
# Fenwick trees are powerful for range sum queries especially when updates and sum queries.
# It is also very easy to code over segment trees.
# -------------------------------------------------------------------------
# Idea is based on binary representation of numbers.
# So, basically fenwick trees uses the same memory size as the original array.
# Then, we can visualize the array as tree structure where every node doesn't only contains it's own value but also
# considers more values (maximum log(N)) times.
# --------------------------------------------------------------------------
# Updates : 0(log(N))
# range query : 0(Log(N))
# BUILDING FROM ARRAY : 0(N*log(N))
# -------------------------------------------------------------------------
# also called binary-indexed-tree (BIT)
# stores the sum in same way as prefix array [0.....index]
# -----------------------------------------------------------------------
# we always consider more than one extra node starting from 0.....

class FenwickTree:

    def __init__(self, size):
        self.size = size
        self.BIT = [0] * (self.size + 1)

    # add all the value upto the ancestors
    def get_sum(self, i):
        sum = 0
        i += 1
        while i > 0:

            sum += self.BIT[i]

            # getting parent index
            i -= i & (-i)

        return sum

    # update at that index, and traverse upto ancestors
    def update(self, i, v):

        i += 1

        while i <= self.size:

            self.BIT[i] += v

            # update index to that of parent
            i += i & (-i)

    # building the tree takes 0(N*log(N))
    def build(self, arr):

        for i in range(len(arr)):
            self.update(i, arr[i])

    def pretty_print(self):
        print(self.BIT)

if __name__ == '__main__':
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = FenwickTree(len(freq))
    # for range queris for [l, r] apply  : get_sum(r) - get_sum(l - 1)
    bit.build(freq)
    print(bit.get_sum(5))
    # for range queries:
    l, r = 3, 5
    print(bit.get_sum(r) - bit.get_sum(l - 1))
