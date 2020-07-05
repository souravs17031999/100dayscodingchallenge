# program for computing median and outputting it given as a stream of integers (online algorithms)
# The idea is that we observe that when we have a median element (let's say first one), then if the next element
# is greater than current median, then new median is either the same or average of cur and next (depenedent on only these two)
# similary, for next elements smaller than cur median, it is again either the same or avg of the two
# this depends on the length of the heap which is dynamically changing.
# So, to keep a track of just smaller element and just greater element being added, we need a binary heap.
# Here, we are required to use two heaps : maxheap for left side, minheap for right side.
# We at any point of time, maintain two heaps - min-heaps and max-heaps onto which new element goes depending upon if it is
# smaller or greater than median - max heap / min heap resepctively.
# Also, we get the median as the top of the heap containing max elements because median has obviously shifted to that side.
# If both have the same elements, then we get the avergae of the two elements at the top of both heaps.


from heapq import heappop, heappush, heapify

def StreamMedian():
    lheap, rheap = [], []
    heapify(lheap)
    heapify(rheap)

    n = int(input())
    heappush(lheap, -n)

    med = n
    print(f"med : {med}")
    while 1:
        n = int(input())
        if len(lheap) > len(rheap):
            if n <= med:
                heappush(rheap, -heappop(lheap))
                heappush(lheap, -n)
            else:
                heappush(rheap, n)

            med = (-lheap[0] + rheap[0]) / 2

        elif len(lheap) == len(rheap):
            if n <= med:
                heappush(lheap, -n)
                med = -lheap[0]
            else:
                heappush(rheap, n)
                med = rheap[0]
        else:
            if n >= med:
                heappush(lheap, -heappop(rheap))
                heappush(rheap, n)
            else:
                heappush(lheap, -n)

            med = (-lheap[0] + rheap[0]) / 2

        print(f"med : {med}")




if __name__ == '__main__':
    StreamMedian()
