# Program to merge k sorted arrays but now of different sizes.
# Earlier when sizes were same, then we could have used DAC approach to break down the problem and
# merge into groups of 2 by recursive method.
# But now since sizes are different, it is not feasible to exactly break these in groups of 2.
# Hence, for this only one optimized solution could be there  - to use binary min heap of size k.
# TIME : 0(N*lg(k)), SPACE : 0(K)


from heapq import heappush, heappop, heapify

# OPTMIZED SOLUTION :
def MergeKSortedarrays(arr, k):
    # build and initalize the heap of size k
    heap = []
    heapify(heap)
    for i in range(k):
        heappush(heap, (arr[i][0], i, 0))

    # heap.print_heap()
    res = []
    # heap.print_heap()
    # Iterate while heap is not empty
    while heap:
        # get the top element along with i, j entry of the array
        element, x, y = heap[0]
        # took off the root element
        heappop(heap)
        # push to the result
        res.append(element)
        # we check whether our current row of array exhausts, if yes then we do nothing
        if (y + 1 < len(arr[x])):
            heappush(heap, (arr[x][y + 1], x, y + 1))
        # heap.print_heap()
    return res



if __name__ == '__main__':
    arr1 = [[2, 6, 12], [1, 9], [23, 34, 90, 2000]]
    k = 3
    print(MergeKSortedarrays(arr1, k))
