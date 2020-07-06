# Program for sorting nearly k-sorted arrays, where k means elements can be atmost
# k positions from the current element.
# IDEA: So, naive idea is to simply sort the entire array ingoring the valuable info of k , and
# this would do no better than (N*lg(N)).
# Now, optimized approach :
# To think about this, we need to critically think about the information K gives us, like
# the element can end up at either same position or atmost k postions in either left or right direction of current position after sorting.
# That also, means that we have defined set of possibilities - for solution spaces.
# And now if we observe then, we can k + 1 possibilities for each position (can be seen by drawing out a example) and we need to get minimum
# for each of those k possibilities at each position and that can only be done efficiently using binary min-heap.
# So, we can insert first k + 1 elements in min heap, then pop out each element at a time and then insert next element from remaining element
# from the array.
# TIME : 0(N*lg(K)), SPACE : 0(K)

from heapq import heappush, heappop, heapify

def SortArray(arr, k):

    n = len(arr)
    # heapify by taking first k + 1 elements
    heap = arr[:k + 1]
    heapify(heap)

    target_idx = 0
    # one by one take off root and copy to the sorted array and
    # then push new element into the heap
    for i in range(k + 1, n):
        arr[target_idx] = heappop(heap)
        heappush(heap, arr[i])
        target_idx += 1

    # there are some remaining elements after the above loop is over
    # so, simply pop and copy them to the output array
    while heap:
        arr[target_idx] = heappop(heap)
        target_idx += 1

    return arr

# driver test function
if __name__ == '__main__':
    arr = [2, 6, 3, 12, 56, 8]
    print(SortArray(arr, 3))
