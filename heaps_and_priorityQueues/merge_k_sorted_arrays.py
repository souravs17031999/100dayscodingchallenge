from heapq import heappush, heappop, heapify
# Program for merging k number of arrays of given size n
# It is also possible for the size n to be a variable
# IDEA: Naive solution is to simply keep merging one by one all the arrays in groups of 2,
# like merge subroutine, but since total time for merging the two arrays will be n*lg(nk),
# and since there are k arrays, hence, total time will be n*k*lg(nk), space : 0(n * k)
# Second approach will be to use Divide and conquer approach as we can see here we can
# break down the problem into smaller subproblems, and then combine them like mergesort.
# So, we can try to divide the arrays in groups of 2, until only one of them is left, which is simply copied to output array
# and when two of them are left we try to merge them and return.
# otherwise keep dividing them recursively.
# Finally all the arrays obtained using above steps.
# This will take 0(n * k * lg(k)) and space : 0(n * k * log(k))


# Now OPTIMIZED APPROACH : idea is to use merge subroutine but not using exact pointers as we don't know how many arrays will be there beforehand ,
# and can't hardcode the pointers and since we wanna know the minimum of all the elements pointers one by one and select them and copy to the output array
# a binary min heap is really efficient as the root can give us the min in 0(1) time everytime we push the pointers (heads) of all arrays in the k-sized
# heap constructed.
# We remove the root element copy it to the output array and then take push the next element from the array where root element was removed as it's pointers
# have advanced (similar to like merge subroutine)
# TIME : 0(n*k*lg(k)), SPACE : 0(K)

# OPTMIZED SOLUTION :
def MergeKSortedarrays(arr, k, n):
    # build and initalize the heap of size k
    heap = []
    heapify(heap)
    for i in range(k):
        heappush(heap, (arr[i][0], i, 0))

    # heap.print_heap()
    res = [0] * (n * k)
    # heap.print_heap()
    k = 0
    # Iterate while heap is not empty
    while heap:
        # get the top element along with i, j entry of the array
        element, x, y = heap[0]
        # took off the root element
        heappop(heap)
        # push to the result
        res[k] = element
        k += 1
        # we check whether our current row of array exhausts, if yes then we do nothing
        if (y + 1 < len(arr[x])):
            heappush(heap, (arr[x][y + 1], x, y + 1))
        # heap.print_heap()
    return res

# # SECOND solution :
# def merge(arr1, arr2, n1, n2, arr3):
#     arr1_size, arr2_size = n1, n2
#     if arr1_size == 0:
#         return arr2
#     if arr2_size == 0:
#         return arr1
#     # third array for returning sorted elements
#     i, j, k = 0, 0, 0
#     # looping over the both the arrays
#     while(i < arr1_size and j < arr2_size):
#         # if first array element is smaller
#         if arr1[i] < arr2[j]:
#             arr3[k] = arr1[i]
#             i += 1
#         # if second array element is smaller
#         else:
#             arr3[k] = arr2[j]
#             j += 1
#         k += 1
#     # executes copying if remaining elements are from array 1
#     while i < arr1_size:
#         arr3[k] = arr1[i]
#         i += 1
#         k += 1
#     # executes copying if remaining elements are from array 2
#     while j < arr2_size:
#         arr3[k] = arr2[j]
#         k += 1
#         j += 1
#
#
# def MergeKSortedarrays(arr, i, j, output):
#     if i == j:
#         for p in range(0, n):
#             output[i] = arr[i][p]
#             return
#
#     if (j - i == 1):
#         merge(arr[i], arr[j], n, n, output)
#         return
#
#     out1, out2 = [0] * n*(((i+j)//2)-i+1), [0] * n*(j-((i+j)//2))
#     MergeKSortedarrays(arr, i, (i + j) // 2, out1)
#     MergeKSortedarrays(arr, (i + j) // 2 + 1, j, out2)
#
#     merge(out1, out2, n*(((i+j)//2)-i+1), n*(j-((i+j)//2)), output)

if __name__ == '__main__':
    mat = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
    ]
    arr = [
        [2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]
    ]
    k, n = 3, 4
    print(MergeKSortedarrays(mat, k, n))
    print(MergeKSortedarrays(arr, k, n))
