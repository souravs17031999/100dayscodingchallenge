# Program to build and query segment trees
# Template for solving questions for range query questions.
# Queries for segment trees : 0(log(N)),
# building segment trees from array : 0(N).
# ----------------------------------------------------------------------------
# Logic is to start from root which contains complete range value [0.....n]
# Now, at every node we split the node into two equal halves, and left = [0.....n/2],
# right = [n/2 + 1.......n]
# left index = 2 * i + 1, right index : 2 * i + 2, i is index of parent (root).
# So, when querying we have three cases :
# either our current node range (low, high) will be in given range(l, r), so we retunr the direct answer stored in that node.
# otherwise if our range is not in given range(l, r), that is our of bounds, then we need to return "the value that depends on question".
# like it can be INT_MIN for max range queries.
# Else, if it overlaps, meaning some part of our range lies in the given range, then it means we need to call left and right subtree to combine
# our answer from both of its parts.
# ---------------------------------------------------------------------------
# Segment trees can be very powerful for range queries problems like max, min for range queries (l, r), sum etc...
# ----------------------------------------------------------------------------
# The below code is for min range query, and we need to just change few lines for max, sum queries....

import sys
class SegmentTree:

    def __init__(self, size):
        self.MAX_SIZE = 4 * size
        self.seg = [None] * self.MAX_SIZE

    def build(self, i, low, high):

        if low == high:
            self.seg[i] = arr[low]
            return

        mid = (low + high) // 2
        self.build(2 * i + 1, low, mid)
        self.build(2 * i + 2, mid + 1, high)
        self.seg[i] = max(self.seg[2 * i + 1], self.seg[2 * i + 2]) # change this acc. to question

    def query(self, i, low, high, l, r):

        if low >= l and high <= r:
            return self.seg[i]

        if high < l or low > r:
            return -sys.maxsize-1  # change this acc. to question

        mid = (low + high) // 2
        left = self.query(2 * i + 1, low, mid, l, r)
        right = self.query(2 * i + 2, mid + 1, high, l, r)
        return max(left, right) # change this acc. to question

    def update(self, i, low, high, node, value):
        if low == high:
            self.seg[low] += value
        else:
            mid = (low + high) // 2
            if node <= mid and node >= low:
                self.update(2 * i + 1, low, mid, node, value)
            else:
                self.update(2 * i + 2, mid + 1, high, node, value)

            self.seg[i] = max(self.seg[2 * i + 1], self.seg[2 * i + 2])  # change this acc. to question

    def pretty_print(self):
        print(self.seg)

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(len(arr))
    st.build(0, 0, len(arr) - 1)
    st.pretty_print()
    print(st.query(0, 0, len(arr) - 1, 1, 3))
