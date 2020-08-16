# Program for building min-heap from scratch using underlying lists (arrays)
# We have implemented all safety overflow and underflow checks.
# All the insertions like insertions, deletion, updations take 0(lg(N)) time,
# heapify also takes (lg(N)) time.
# Getting min/max takes 0(1) time depending on min-heap/max-heap.

import random

# class structure for heaps
class MinHeap:

    def __init__(self, maxsize = 10):
        '''
        maxsize : maxsize is default 10, otherwise we can set it.
        '''
        self.maxsize = maxsize
        # we initialize a list of maxsize elements to avoid extending lists every time.
        self.heap = [0] * (maxsize)
        # it keeps a track of current size of actual heap.
        self.size = 0

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
    def heappush(self, x):
        self.size += 1
        if self.size > self.maxsize:
            raise Exception ("Heap Overflow reached !")

        print(f"current heap size : {self.size}")
        self.heap[self.size - 1] = x
        idx = self.size - 1
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]

            idx = self.parent(idx)

    # function for heapfiying
    def MinHeapify(self, i):
        # we initialize the largest to be current element (element to be swapped)
        smallest = i
        left = 2 * i + 1  # extract left index
        right = 2 * i + 2 # extract right index

        # we compare the left child with the current element and set it largest if its maximum that current element
        if left < self.size and self.heap[left] < self.heap[i]:
            smallest = left

        # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        # if there is a change in largest, it means there is voilation of heap property and we need to swap
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # call heapify recursively for every node one by one top to down
            self.MinHeapify(smallest)


    # function for popping from the heap
    def heappop(self):
        if self.size:
            pop_value = self.heap[0]
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            # del self.heap[self.size - 1]
            self.size -= 1
            self.MinHeapify(0)
            return pop_value
        else:
            raise Exception ("Heap is already empty !")

    # function to get minimum from the heap
    def getMin(self):
        if self.size:
            return self.heap[0]
        else:
            raise Exception ("Index doesn't exist !")

    # printing the heap
    def printheap(self):
        if self.size:
            for i in range(self.size):
                print(self.heap[i], end = " ")
            print()
        else:
            raise Exception ("Empty heap !")


# driver testing function
if __name__ == '__main__':
    heap = MinHeap()
    l = [random.randint(0, 1000) for _ in range(10)]
    print(l)
    for i in l:
        heap.heappush(i)

    heap.printheap()
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    heap.printheap()
    print(f"Min : {heap.getMin()}")
