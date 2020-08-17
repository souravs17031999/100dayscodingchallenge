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
        self.seg[i] = self.seg[2 * i + 1] ^ self.seg[2 * i + 2] # change this acc. to question

    def query(self, i, low, high, l, r):

        if low >= l and high <= r:
            return self.seg[i]

        if high < l or low > r:
            return 0  # change this acc. to question

        mid = (low + high) // 2
        left = self.query(2 * i + 1, low, mid, l, r)
        right = self.query(2 * i + 2, mid + 1, high, l, r)
        return left ^ right # change this acc. to question

    def update(self, i, low, high, node, value):
        if low == high:
            print("value updated")
            self.seg[low] = value
        else:
            mid = (low + high) // 2
            if node <= mid and node >= low:
                self.update(2 * i + 1, low, mid, node, value)
            else:
                self.update(2 * i + 2, mid + 1, high, node, value)

            self.seg[i] = self.seg[2 * i + 1] ^ self.seg[2 * i + 2]  # change this acc. to question

    def pretty_print(self):
        print(self.seg)

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(len(arr))
    st.build(0, 0, len(arr) - 1)
    print(st.query(0, 0, len(arr) - 1, 1, 3))
    st.update(0, 0, len(arr) - 1, 1, 10)
    print(st.query(0, 0, len(arr) - 1, 1, 3))
