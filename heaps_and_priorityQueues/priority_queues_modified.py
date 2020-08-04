# This priority queue has been modified and extended to accomodate a extra hashmap which maps the label nodes values
# with their exact index into the heap array.
# since, it's not necessary that tuple having "1" in value pos, will be always in the first index of heap,
# and so we need a mapping to map it to exact index in the heap array.
# -------------------------------------------------------------------------------
# This is particularly useful for Dijskstra's algo and MST graph algorithms, where we need decrease_key operation
# and we simply send the key and now using map, we get exact index, and then update the heap value and restore heap.
# ------------------------------------------------------------------------------------
# 

import random
from string import punctuation
import string

class PriorityQueue:

    def __init__(self, maxsize):

        # we initialize a list of maxsize elements to avoid extending lists every time.
        self.heap = [[None, None] for _ in range(maxsize)]
        # it keeps a track of current size of actual heap.
        self.size = 0
        # mapping of actual elements
        self.map = [None] * maxsize

    # helper function for getting parent of any node at index i
    def parent(self, i):
        return (i - 1) // 2

    # helper function for getting left child of any node at index i
    def left(self, i):
        return 2 * i + 1

    # helper function for getting right child of any node at index i
    def right(self, i):
        return 2 * i + 2

    # function for pushing the element onto heap
    def heappush(self, priority, val):

        self.size += 1
        idx = self.size - 1
        self.heap[idx][0], self.heap[idx][1] = priority, val
        self.map[idx] = val
        while idx > 0 and self.heap[self.parent(idx)][0] > self.heap[idx][0]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]
            self.map[self.parent(idx)], self.map[idx] = self.map[idx], self.map[self.parent(idx)]

            idx = self.parent(idx)

    # function for heapfiying
    def MinHeapify(self, i):
        # we initialize the largest to be current element (element to be swapped)
        smallest = i
        left = 2 * i + 1  # extract left index
        right = 2 * i + 2 # extract right index

        # we compare the left child with the current element and set it largest if its maximum that current element
        if left < self.size and self.heap[left][0] < self.heap[i][0]:
            smallest = left

        # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        # if there is a change in largest, it means there is voilation of heap property and we need to swap
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.map[i], self.map[smallest] = self.map[smallest], self.map[i]
            # call heapify recursively for every node one by one top to down
            self.MinHeapify(smallest)

    # function for popping from the heap
    def heappop(self):
        pop_value = self.heap[0][0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.map[0], self.map[self.size - 1] = self.map[self.size - 1], self.map[0]
        del self.heap[self.size - 1]
        self.map[self.size - 1] = None
        self.size -= 1
        self.MinHeapify(0)
        return pop_value

    # function to get minimum from the heap
    def getHighestPriority(self):
        if self.size:
            return self.heap[0]
        else:
            raise Exception ("Index doesn't exist !")

    def decrease_key(self, i, new_val):
        i = self.map[i]
        self.heap[i] = [new_val, i]
        while i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            self.map[i], self.map[self.parent(i)] = self.map[self.parent(i)], self.map[i]

    # printing the heap
    def printheap(self):
        if self.size:
            print(f"heap : {self.heap}")
            print(f"map : {self.map}")
            print()
        else:
            raise Exception ("Empty heap !")

# driver testing function
if __name__ == '__main__':
    q = PriorityQueue(5)
    q.heappush(1000, 1)
    q.heappush(90, 2)
    q.heappush(0, 0)
    q.printheap()
    q.decrease_key(1, 5)
    q.printheap()
    q.decrease_key(2, 3)
    print(q.heappop())
    print(q.heappop())
    print(q.heappop())
