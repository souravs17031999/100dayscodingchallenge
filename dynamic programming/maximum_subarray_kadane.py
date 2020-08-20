# Program for computing maximum sum subarray for the given array
# ----------------------------------------------------------------------------------
# Naive solution would be to fix left pointer and for every left pointer, move right pointer and then
# in this way we can generate all the sums possible for all the subarrays in the array but this will take 0(N^3).
# Can we do better ?
# Yes, As we can see the sum we are calculating is being duplicated and repeated work as we calculate sum for [0...N],
# and when we compute for [1.....N], there are problems which are overlapping which gives us hint for DP.
# At every point, we ask if the current element can be taken (forgetting about last progress) or if current element can be included in the
# last progress made so far.

# In reality, we can use extra 1 -D array to store the solutions of subproblems but we can get away with it using
# one extra variable which can keep track of curr_sum (current maximum till current index).

# ALgorithm here is Kadane's algo which takes 0(N) with 0(1) space.
# This is a variant of window sliding technique. (sliding window + DP)

import sys
def maxSubArray(nums):
    curr_sum, max_sum = 0, -sys.maxsize-1
    for i in range(len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

# if we want the starting and ending indices for max subarray :

# def maxSubArray(nums):
#     curr_sum, max_sum = 0, -sys.maxsize-1
#     start, end, s = 0, 0, 0
#     for i in range(len(nums)):
#         curr_sum += nums[i]
#         if curr_sum < nums[i]:
#             curr_sum = nums[i]
#             s = i
#
#         if max_sum < curr_sum:
#             max_sum = curr_sum
#             start = s
#             end = i
#
#     print(f"start : {start}, end : {end}")
#     return max_sum


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArray(arr))
