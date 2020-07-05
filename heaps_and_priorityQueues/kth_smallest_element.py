# Program to find kth smallest element in the given array
# IDEA: Naive solution is to simply sort the array and then return the kth index but this would do no better than 0(N*lg(N)).
# One optimized version is to use binary min-heap, which will actually return the kth element in kth extracting min from the root.
# This would take N + k*lg(N) time with space : 0(N)

# BElow approach is heap approach
from heapq import heappush, heappop, heapify

def KSmallestHeap(arr, k):
    heapify(arr)
    res = None
    for i in range(k):
        res = heappop(arr)

    return res

# Another thing is one where we can have expected linear time complexity , and other where we can have guaranateed
# linear time complexity

# BElow is expected linear time based on the idea of partition function of quicksort and DAC approach:
# So, again we can observe that this can be solved using DAC approach as we can simply reduce the problem to subproblem
# let's say if we know our kth element is not in some subarray, then we can simply ignore that part and continue our search in recursive fashion.
# We also use randomization such that it is assumed that every element is likely selected to be pivot element for partition.

import random
def partition(arr,low,high):
    print(low, high)
    i = low - 1
    pivot = arr[high]
    for j in range(low , high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partitionr(arr, low, high):
	randpivot = random.randrange(low, high)
	arr[low], arr[randpivot] = arr[randpivot], arr[low]
	return partition(arr, low, high)

def KSmallestQuick(arr, l, h, k):

    while l <= h:
        p = partitionr(arr, l, h)
        if p == k:
            return arr[p]
        elif p > k - 1:
            h = p - 1
        else:
            l = p + 1

    return -1

# More solutions can be there which are linear time optimized
# Counting sort is one of them, giving time : 0(N), space : 0(M), M is maximum of given array.

def KSmallestCountSort(arr, K):
    k = max(arr) + 1
    # output for sorted array
    output = [0 for _ in range(len(arr))]
    # count storage , auxiliary array
    count = [0 for _ in range(k)]
    # compute frequecnies
    for i in range(len(arr)):
        count[arr[i]] += 1
    # compute prefix sum
    for i in range(1, k):
        count[i] += count[i - 1]
    # finally, placing input elements in their correct positions , going from back to produce stable sort ,
    # otherwise traversing from front will also work but not stable
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output[K - 1]

if __name__ == '__main__':
    arr =  [12, 3, 5, 7, 19]
    k = 2
    # print(KSmallestHeap(arr, k))
    print(KSmallestCountSort(arr, k))
    #print(KSmallestQuick(arr, 0, 4, k))
