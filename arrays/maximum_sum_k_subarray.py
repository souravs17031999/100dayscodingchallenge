# program for finding the maximum sum of array for k consecutive array elements
# Naive solution will be to simply generate all the subarrays of length "k" and get the sum along with it also keeping and maintaining max_sum, 
# Now, this would take brute force in 0(N * k * k) but with little optimization, we can take the sum along as we go on generating the subarrays, so, it would be done in 0(N * k).
# But can we do more better than this ?
# For that, we should firstly understand what is the bottleneck for the program ?
# Let's see : 
# arr : [100, 200, 300, 400], K = 2 (window size)
# Now, we can generate all subarrays :
# [100                      -----------------------
# [100, 200                                       |
# [100, 200, 300                                   
# [100, 200, 300, 400                                       =>  take sum along with generating one by one and check for max_sum so far 
# [200, 
# [200, 300                                       | 
# [200, 300, 400
# [300, 
# [300, 400                                       |
# [400                    -------------------------
# As we can see, sums are being duplicated due to repetitive work in every subarray, 
# so, we need to compute sum only once for every subarray and no need for duplicacy, we can do this using sliding window concept.
# 
#
#  |100, 200| 300 400 is our first window, get the sum as 300, now discard first element (100) and include next element to form next valid window 
#  100 |200, 300| 400 => 500
#  100 200 |300 400| => 700
#  So, 700 is maximum sum for k = 2.
# 
# Best optimized solution would be to basically use window sliding approach , which creates and keeps track of just two pointers start and end,
# and keep sliding one at a time and taking sum simulatenously.
# Time : 0(N), space : 0(1)
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# MORE CLEARER WAY FOR USING SLIDING WINDOW APPROACH : 

import sys 
def max_sum_subarray(arr, k):
    
    n = len(arr)
    if n < k:
        print("INVALID")
    start = 0
    count = 0
    max_sum = -sys.maxsize-1
    temp_sum = 0
    for end in range(n):
        count += 1
        temp_sum += arr[end]
        if count == k:
            max_sum = max(temp_sum, max_sum)
            temp_sum -= arr[start]
            start += 1
            count -= 1
    
    print(max_sum)

max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)

# ATERNATE WAY FOR DOING SAME APPROACH (WITH COMMENTS): 

# above required function
def max_k_sum(arr, k):
    arr_size = len(arr)
    # obviously, if k is greater than length of arr, then its invalid
    if k > arr_size:
        return -1
    # keep two pointers one at start, one at window maximum size
    # one can get away with these two pointers by just using loop variables
    start = 0
    end = k - 1
    # storing first window sum
    curr_sum = max_sum = sum(arr[:k])
    # lopping the whole pane using one at a time
    for i in range(arr_size - k):
        start += 1
        end += 1
        # calculating current sum of window by neglecting last left element and including latest element in the window
        curr_sum = curr_sum - arr[start - 1] + arr[end]
        # getting the overall maximum so far
        max_sum = max(max_sum, curr_sum)
    return max_sum

# main function 
if __name__ == '__main__':
    assert max_k_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    assert max_k_sum([100, 200, 300, 400], 2) == 700
    assert max_k_sum([2, 3], 3) == -1
    assert max_k_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4) == 24
