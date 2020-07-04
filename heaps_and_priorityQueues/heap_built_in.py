# Program for implementing heaps using built-in modules
# By default, min-Heap is implemented and Max heap can be implemented by multiplying by "-1" while doing any operation.
# All insertions and deletions take 0(lg(N)) time, getting min and max is done in 0(1).

import random
from heapq import heappush, heappop, heapify, nsmallest, nlargest

# initializing the heap from empty list using heapfiy
heap = []
heapify(heap)

# constructing randomzied elements to be pushed into heapify
print("MIN-HEAP : ")
l = [random.randint(0, 1000) for _ in range(10)]

# pushing into min heap
print(l)
for i in l:
    heappush(heap, i)

# printing the min heap
for i in range(len(heap)):
    print(heap[i], end = " ")

# getting the minimum from min heap
print(f"\nMin from heap : {heap[0]}")

# popping the element from min heap
print(f"popped from heap : first : {heappop(heap)} second : {heappop(heap)}")

# getting top 3 largest, top 3 smallest from min heap
print(f"TOP 3 smallest : {nsmallest(3, heap, key = lambda x : x)}")
print(f"TOP 3 largest : {nlargest(3, heap, key = lambda x : x)}")

# constructing max heap
mheap = []
heapify(mheap)
print("MAX-HEAP")
print(l)
# pushing into max heap
for i in l:
    heappush(mheap, -i)

# printing the max heap
for i in range(len(mheap)):
    print(-mheap[i], end = " ")

# getting the max element from max heap
print(f"\nMin from heap : {-mheap[0]}")

print(f"popped from heap : first : {-heappop(mheap)} second : {-heappop(mheap)}")
