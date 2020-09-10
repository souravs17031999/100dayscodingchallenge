# Program for finding the pair whose sum is closest to x.

# Input: nums = [1, 2, 3, 4, 5], target = 10
# Output: [4, 5]
# Input: nums= [-1, 2, 1, -4], target = 4
# Output: [2, 1]
# --------------------------------------------------------------------------------------------------------------------
# TIME : 0(N * LOG(N)), BECAUSE ARRAY IS NOT UNSORTED but if array is sorted,
# then, TIME : 0(N)

import sys
def compute_closest_pair(arr, n, x):

    l_idx, r_idx, diff =  0, 0, sys.maxsize
    left, right = 0, n - 1
    arr.sort()
    while left < right:

        if abs(arr[left] + arr[right] - x) < diff :
            l_idx = left
            r_idx = right
            diff = abs(arr[left] + arr[right] - x)

        if arr[left] + arr[right] > x:
            right -= 1
        else:
            left += 1

    return [arr[l_idx], arr[r_idx]]

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    assert compute_closest_pair(arr, len(arr), 10) == [4, 5]
