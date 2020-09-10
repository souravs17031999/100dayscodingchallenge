# Program for computing smallest subarray size which has sum greater than or equal to K.
# Input: A[] = {2, -1, 2}, K = 3
# Output: 3
# Explanation:
# Sum of the given array is 3.
# Hence, the smallest possible subarray satisfying the required condition is the entire array.
# Therefore, the length is 3.
#
# Input: A[] = {2, 1, 1, -4, 3, 1, -1, 2}, K = 5
# Output: 4
# ----------------------------------------------------------------------------------------------------
# Naive solution will be to generate all the possible substrings and check the sum if found correct acc. to constrainsts,
# then update the length found min so far and return the overall minimum length, but this will take 0(N^3).
# Can we do better ?
# Yes, we can and we will use window sliding , dynamic variant.
# As we can see, we can't get smallest window in one traversal for the same sized window, therefore we need to first get the
# window which has correct constrainsts and then shrink from left side to minimize it and get the minimum overall.

# ---------------------------------------------------------------------------------------------------------
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
