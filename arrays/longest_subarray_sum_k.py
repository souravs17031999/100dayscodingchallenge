# Program for finding the length of longest subarray whose sum equals to "K".
# Examples:
#
# Input : arr[] = { 10, 5, 2, 7, 1, 9 }, 
#            k = 15
# Output : 4
# The sub-array is {5, 2, 7, 1}.
#
# Input : arr[] = {-5, 8, -14, 2, 4, 12},
#            k = -5
# Output : 5
# -------------------------------------------------------------------------------------------------------------------------------
# Naive Approach: Consider the sum of all the sub-arrays and return the length of the longest sub-array having sum ‘k’. Time Complexity is of O(n^2).
# Can we do better ? 
# Yes, we are going to use Dynamic Sliding Window + Hashing.
# So, here we don't know about fixed size window as the window itself is to be found, so firstly we will be iterating and get the valid window, after then we can update the 
# max_length of subarray, now, once we get the sum till index "i", we can;t go back and start new subarray as in naive approach, so we will save all the prefix sums being 
# generated will be saved in Hashmap with key as sums, and value as index of first occurence.
# So, we can two ways of updating the max_len, 
# Now, we can keep iterating summing up the elements, check if it equals "K", which will update max_len, otherwise we can check if the sum-k, value is stored in map, that means 
# remaining subarray will have sum=k, and the lenght of this subarray will be "i-map[sum-k]" and update max_len, if necessary.
# Following is simulation of above algo : 
#
# ^ shows end pointer of sliding window 
# 10, 5, 2, 7, 1, 9 => sum => 10, max_len = 0, map : {10:0}
#  ^
# 10, 5, 2, 7, 1, 9 => sum => 15, max_len = 2, map : {10:0, 15:1}
#     ^
# 10, 5, 2, 7, 1, 9 => sum => 17, max_len = 2, map : {10:0, 15:1, 17:2}
#        ^
# 10, 5, 2, 7, 1, 9 => sum => 24, max_len = 2, map : {10:0, 15:1, 17:2, 24:3}
#           ^
# 10, 5, 2, 7, 1, 9 => sum => 25, now here also 25-15 => 10 is also in map indicating sliding window [5, 2, 7, 1] => max_len = 4, {10:0, 15:1, 17:2, 24:3, 25:4}
#              ^
# 10, 5, 2, 7, 1, 9 => sum => 34, max_len = 4, {10:0, 15:1, 17:2, 24:3, 25:4, 34:5}
#                 ^
# ----------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)

def longest_subarray_sum(arr, n, k):
    
    temp_sum = 0
    max_len = 0
    map = {}  # store : prefix_sum_from_0_till_i:start_index(i)
    for end in range(n):
        
        temp_sum += arr[end]
        if temp_sum == k:
            max_len = end + 1
        
        elif temp_sum - k in map:
            max_len = max(max_len, end - map[temp_sum - k])
        
        if temp_sum not in map:
            map[temp_sum] = end
    
    print(max_len)

arr = [10, 5, 2, 7, 1, 9] 
n = len(arr) 
k = 15
longest_subarray_sum(arr, n, k)
