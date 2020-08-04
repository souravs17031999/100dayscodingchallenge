from heapq import heappush, heappop

class PriorityQueue:

    def __init__(self):

        self.heap = []


    # helper function for getting parent of any node at index i
    def parent(self, i):
        return i // 2

    # function for pushing the element onto heap
    def heappush(self, priority, val):

        heappush(self.heap, (priority, val))

    # function for popping from the heap
    def heappop(self):

        return heappop(self.heap)


    def decrease_key(self, i, new_val):
        self.heap[i] = (new_val, i)
        while i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def pretty_print(self):
        print(self.heap)

if __name__ == '__main__':
    queue = PriorityQueue()
    queue.heappush(0, 0)
    queue.heappush(100000, 1)
    queue.heappush(100000, 2)
    queue.heappush(100000, 3)
    temp = queue.heappop()
    queue.pretty_print()
    queue.decrease_key(1, 90000)
    queue.pretty_print()
