# Program for huffman coding algorithm using greedy approach
# We have been given arr containing data, now frequency given associated with data
# and size is total length of array.
# TIME : 0(N*log(N))
# NOTE : given array is not sorted.
# If array is sorted, then we can do this in linear time (can get away with heaps !)

from heapq import heapify, heappush, heappop
class MinHeapNode:

    def __init__(self, val, freq):
        self.data = val
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(arr, freq, size):

    # build all the unique data and push into min heap
    heap = []
    for i in range(size):
        heappush(heap, (freq[i], MinHeapNode(arr[i], freq[i])))

    # for all heap, in the tuple : Ist index : freq, 2nd index : node address
    while len(heap) > 1:


        left = heappop(heap)

        right = heappop(heap)

        new_root = MinHeapNode(left[0] + right[0], '$')

        new_root.left = left[0]
        new_root.right = right[0]

        heappush(heap, (left[0] + right[0], new_root))

    print(heap)


if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    size = 6
    build_huffman_tree(arr, freq, size)
