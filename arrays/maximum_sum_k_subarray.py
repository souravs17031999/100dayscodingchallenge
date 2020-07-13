# program for finding the maximum sum of array for k consecutive array elements
# Best optimized solution would be to basically use window sliding approach , which creates and keeps track of just two pointers start and end,
# and keep sliding one at a time and taking sum simulatenously.
# Time : 0(N), space : 0(1)

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
