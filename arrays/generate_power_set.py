# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
# ]
# ------------------------------------------------------------------------------------------------------------------
# We have already seen binary bit masking approach for generating power set as well as recursion / backtracking approach, we will just visualize the recursion tree call
# for better understanding of power set generation.
# The approach is like at every index of array, we have two choices to make, so we make that choices :
# * either we can include the current element 
# * or we can leave the current element.
# Now, how do we where we are currently standing in the array/string ? We use a pointer var "index" for that.
# Base case will be when our index is out of bounds, that is index == len(arr)/len(s), then we need to print the current subset formed so far.
# for tracking current subset, we can keep a extra list/array for generating subset so far with running elements.
# Following is recursion tree for arr : [1, 2, 3], with index = 0, and temp = []
#                         
#                                            (0, [])
#                                   /                    \
#                        (1, [])                       (1, [1])
#                           /   \                        /   \
#                     (2, [])  (2, [2])           (2, [1])  (2, [1, 2])
#                         / \        /\                / \              / \
#                 (3, []) (3, [3]) (3,[2]) (3,[2,3]) (3,[1]) (3,[1,3]) (3,[1,2]) (3,[1,2,3])
#
#

def subset(arr, index, temp, res):
    
    if index == len(arr):
        res.append(temp)
    else:
        subset(arr, index + 1, temp, res)
        subset(arr, index + 1, temp + [arr[index]], res)

