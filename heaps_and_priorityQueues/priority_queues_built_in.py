# Program for implementing PriorityQueue using built-in modules
# we can use two approach as shown

from heapq import heappush, heappop, heapify
from queue import PriorityQueue

heap = []
heapify(heap)



heappush(heap, (4, 'elon'))
heappush(heap, (1, 'newtech'))
heappush(heap, (3, 'shakti'))
heappush(heap, (2, 'sourav'))
print("PriorityQueue using heapq :")

print(heap)

q = PriorityQueue()
q.put((2, 'sourav'))
q.put((4, 'elon'))
q.put((1, 'shakti'))
q.put((3, 'shakti'))


print("\nPriorityQueue using Queue module, PriorityQueue class :")
# indexing in PriorityQueue is not possible
while not q.empty():
    print(q.get())
