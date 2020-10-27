# program to print maximum of all possible subarrays of k window size
# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
# Output: 3 3 4 5 5 5 6
# All ccontigious subarrays of size k are
# {1, 2, 3} => 3
# {2, 3, 1} => 3
# {3, 1, 4} => 4
# {1, 4, 5} => 5
# {4, 5, 2} => 5
# {5, 2, 3} => 5
# {2, 3, 6} => 6
#
# Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
# Output: 10 10 10 15 15 90 90
# -------------------------------------------------------------------------------------------------------------------------------------
# Naive solution would take 0(N^2) => using two loops, one for outer loop and one inner loop for total array and k size block traversal respectively.

# using deque DS from collections to build linear time solution as following the logic below
# basically, idea is to keep a track of all useful elements for a window which keeps sliding across the array one by one, the useful element is one which
# is greater than all right elements in the current window.
# so, basically for every window we need maximum in 0(1) so that we can compare it with incoming new element and then either keep it or remove it,
# and simulatenously also sliding the window, so the best option is to use Deque so that we will be able to slide the window by popping the elements from
# left side which is not in current window, and also keep track of maximum at the front by comparing it with each incoming element and also one important
# thing is that, we need to keep minimum as it at the right side, as [3...2..0...-1], so if cur_max is 3, then we also need to have 2 because maybe in
# next window, we can have 2 as maximum, threby it will maintain all indices of elements in decreasing order.
# time : 0(N), space : 0(K)

# We can also try window sliding techniuqe and simulate it using two pointers both pointing at start and end of k-sized window.
# Then, we move one pointer one by one k times and update the max, till it becomes equal to second pointer, there we got max for that subarray
# now, we have find the maximum of subarrays of that particular k sized window, then we go for increment second pointer, and then first pointer by 1 from
# last saved first pointer checkpoint.
# In this way, we go through all the subsarrays , this method is actually same as first one, just the way of understanding is different and that's why
# coding is slightly different but overall asymtodic bounds are same => 0(N * K) which is not better but in space it's 0(1).
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import deque
def maximum_subarray(arr, k):
    result = []
    if len(arr) < k:
        return -1
    # Initializing deque
    Q = deque()
    # processing the first k elements
    for i in range(k):
        # keeping only the useful element
        while Q and arr[i] > arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    # processing next remaining elements , n - k
    for i in range(k, len(arr)):
        # the front will always be maximum for current window
        result.append(arr[Q[0]])
        # sliding the window
        while Q and Q[0] <= i- k:
            Q.popleft()

        # again keeping only the useful element
        while Q and arr[i] > arr[Q[-1]]:
            Q.pop()

        Q.append(i)
    # the sliding window stops for last k window, so we need to print explicitly the front for last traversal remaining elements of deque
    result.append(Q[0])

if __name__ == '__main__':
    maximum_subarray([12, 1, 78, 90, 57, 89, 56], 3) == [78, 90, 90, 90, 89]
    maximum_subarray([12, 1, 78], 3) == [78]
    maximum_subarray([12, 1], 3) == -1
    maximum_subarray([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
