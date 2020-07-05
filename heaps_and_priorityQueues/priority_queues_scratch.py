# Program for building priority queue using binary heaps
# Logic is same as heaps inherently give us highest priority elements at the top
# so, we build it in a way that it is now maintaining heap property based on priorities
# We have used 2-d nested list the first of which contains the actual value, second one contains priority associated with the element
# All the operations and complexity bounds are same as was in heaps.

import random
from string import punctuation
import string

class PriorityQueue:

    def __init__(self, maxsize = 10):
        '''
        maxsize : maxsize is default 10, otherwise we can set it.
        '''
        self.maxsize = maxsize
        # we initialize a list of maxsize elements to avoid extending lists every time.
        self.heap = [[None, -1] for _ in range(maxsize)]
        # it keeps a track of current size of actual heap.
        self.size = 0

    # helper function for getting parent of any node at index i
    def parent(self, i):
        return i // 2

    # helper function for getting left child of any node at index i
    def left(self, i):
        return 2 * i + 1

    # helper function for getting right child of any node at index i
    def right(self, i):
        return 2 * i + 2

    # function for pushing the element onto heap
    def push(self, priority, val):
        self.size += 1
        if self.size > self.maxsize:
            raise Exception ("Heap Overflow reached !")

        # print(f"current heap size : {self.size}")
        self.heap[self.size - 1][0] = val
        self.heap[self.size - 1][1] = priority
        idx = self.size - 1
        while idx > 0 and self.heap[self.parent(idx)][1] > self.heap[idx][1]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]

            idx = self.parent(idx)

    # function for heapfiying
    def MinHeapify(self, i):
        # we initialize the largest to be current element (element to be swapped)
        smallest = i
        left = 2 * i + 1  # extract left index
        right = 2 * i + 2 # extract right index

        # we compare the left child with the current element and set it largest if its maximum that current element
        if left < self.size and self.heap[left][1] < self.heap[i][1]:
            smallest = left

        # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
        if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right

        # if there is a change in largest, it means there is voilation of heap property and we need to swap
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # call heapify recursively for every node one by one top to down
            self.MinHeapify(smallest)

    # function for popping from the heap
    def ExtractMax(self):
        if self.size:
            pop_value = self.heap[0][0]
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            del self.heap[self.size - 1]
            self.size -= 1
            self.MinHeapify(0)
            return pop_value
        else:
            raise Exception ("Heap is already empty !")


    # function to get minimum from the heap
    def getHighestPriority(self):
        if self.size:
            return self.heap[0]
        else:
            raise Exception ("Index doesn't exist !")

    # printing the heap
    def printheap(self):
        if self.size:
            print("Current PriorityQueue : ")
            print(self.heap)
        else:
            raise Exception ("Empty heap !")

# driver testing function
if __name__ == '__main__':
    q = PriorityQueue()
    l = ["".join(random.sample(string.ascii_letters, 6)) for _ in range(10)]
    # print(l)
    priority = 1
    for i in l:
        q.push(priority, i)
        priority += 1

    q.printheap()
    print(f"highest priority : {q.ExtractMax()}")
    print(f"second highest priority : {q.getHighestPriority()}")
