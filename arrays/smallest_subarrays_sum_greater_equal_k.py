# Program for computing smallest subarray size which has sum greater than or equal to K.
# Examples: 
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# arr[] = {1, 4, 45, 6, 0, 19}
# x  =  51
# Output: 3
# Minimum length subarray is {4, 45, 6}
#
#arr[] = {1, 10, 5, 2, 7}
#   x  = 9
# Output: 1
# Minimum length subarray is {10}
#
# arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
#    x = 280
# Output: 4
# Minimum length subarray is {100, 1, 0, 200}
#
# arr[] = {1, 2, 4}
#    x = 8
# Output : Not Possible Whole array sum is smaller than 8.
# ----------------------------------------------------------------------------------------------------
# Naive solution will be to generate all the possible substrings and check the sum if found correct acc. to constrainsts,
# then update the length found min so far and return the overall minimum length, but this will take 0(N^3), with little optimization we can achieve in 0(N^2).
# 
# Can we do better ?
# Yes, we can and we will use dynamic window sliding as window size is not fixed, as it is to be found itself.   
# As we can see, we can't get smallest window in one traversal for the same sized window, therefore we need to first get the
# window which has correct constrainsts and then shrink from left side to minimize it and get the minimum overall.
# ---------------------------------------------------------------------------------------------------------
# Logic is to first find the valid window such that sum >= s, no there is no benefit in checking longer than this, so simply start minimizing this window from left, 
# and do it until sum becomes < s, and then start again from right further to find next valid window and repeat it until end of list.
# 
# 2, 3, 1, 2, 4, 3
# ^ 
# start, end
# 2, 3, 1, 2, 4, 3 
# ^........^       => sum = 7, so, we found a valid window now we will minimize it, min_len = 4
# s        e
# 2, 3, 1, 2, 4, 3 => sum = 10, so, we found a valid window, now we will minimize it, min_len = 4
#    ^........^
#    s        e
# 2, 3, 1, 2, 4, 3  => sum = 9, so, we found a valid window, now we will minimize it, min_len = 3
#          ^.....^
# 2, 3, 1, 2, 4, 3   => min_len = 2
#             ^...^
# output : 2
# ------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(1)

import sys
def compute_smallest_subarray(arr, K):

    min_size = sys.maxsize
    curr_window = 0
    start = 0
    for end in range(0, len(arr)):
        curr_window += arr[end]

        while curr_window >= K:
            min_size = min(min_size, end - start + 1)
            curr_window -= arr[start]
            start += 1

    return min_size

if __name__ == '__main__':
    arr = [2, 1, 1, -4, 3, 1, -1, 2]
    K = 5
    print(compute_smallest_subarray(arr, K))
