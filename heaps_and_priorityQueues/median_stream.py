# program for computing median and outputting it given as a stream of integers (online algorithms)

# Naive solution will be to sort the list till current elements everytime we add a new number, that means we maintain a sorted list of numbers.
# Just like a priority Queue implementation, then we need to count if odd or even length, and then return the median.
# Depending upon the above sorted list implementation, assuming array/linked list is used, 0(N^2), where N is length of array.

# -------------------------------------------------------------------------------------------------------------------------------------------------
# Now, we can observe that we actually don't need to maintain complete sorting order for all the elements one by one, as shown below :

# Let's say following elements : [2, 4, 5], 6, [7, 8, 9]
# If we maintain left half sorted in one bucket, and right half sorted in some another bucket, then we can get the median as the average of the top of
# two buckets, and now for getting top of two buckets efficiently, we will use heaps.
# Lower half will use max heap as "5" is the biggest element we need, and right half, "7" is the lowest in its ordering we need to use.
# Then, median  = 5 + 7 // 2 => 6

# At every time, new element is inserted, we need to maintain and balance the heap for the size difference should not be greater than 1, as there are
# only two cases, either total elements can be odd or can be even, so maybe one of the buckets can have one extra element than the another and that is
# okay.
# So, while adding new element, check if balanced, then put in any of them, if unbalanced, then balanced them first by shifting the top from one another.
# Then, while computing median, again check if size difference or same.
# ---------------------------------------------------------------------------------------------------------------------------------------------------

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

# TIME : 0(N*LOG(N))

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
