# Program to compute the first missing positive number in the unsorted array.
# Naive approach to handle this would be to search for atmost n + 1 numbers in the entire array
# and that would tak 0(N^2).
# Can we do better than this ?
# If we do sorting, then obviously, we can do a linear scan to find first positive, and that would
# overall take 0(n*lg(n) + 0(n)), if we do counting sort, then we can reduce it to
# 0(N) time but with extra space of 0(max(arr)).
# We can also build a count array / use HashMaps to do it in 0(N) but again with extra space.
# can we do more better in terms of space efficiency ?
# So, we can apply this trick to treat array numbers as indices, and start a linear scan ,
# and make it negative (* -1) whereever indices exist in the array one by one.
# Now, second time we do linear scan, we will find the only number which is positive is the
# missing number (answer will be index as indices are ordered from 1.....N).
# If we have negative numbers also, we can segragate positive and negative numbers and only
# search for the postive part of the array.
# If the number found in the linear scan is positive, that means that particular index (ans) is
# missing from the array, since if it would not have been missing, then that number should by already
# multiplied by -1 (and the number should have been negative).
# This would take TIME : 0(N) and SPACE : 0(1).

import random

def segregate_array(arr, n):
    j = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j

def compute_missing(arr):

    n = len(arr)
    # we segregate the array into negatives and positives
    idx = segregate_array(arr, n)
    size = n - idx
    # now, we only iterate in the postive part
    # we assume index from 1 to N, since we have to search only postive no.
    for i in range(idx, size):
        # we check if index is valid in the range of size, and if at that
        # place if the number is positve, then make it negative otherwise ignore
        if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    # now , if we found any positive number, then that index is the missing value
    for i in range(size):
        if arr[i] > 0:
            return i + 1

    return size + 1

# ONE more approach we can make in 0(N) time and space 0(1), where
# basically we make the elments appear on their correct indices in the aray.
# So, in the example array : [3, 4, 7, 1]
# We check "3" and put it in 3rd place by swapping it with 7 : [7, 4, 3, 1]
# now, we check "4" but since we don't have valid index, ignore.
# Now, we check "3" since it is already at its own position, so ignore.
# Now, 1 so we swap with 7  : [1, 4, 3, 7].
# Now, we check and find first number which is not in its place,
# that index will be our answer, clearly "2" index number "4" is not in its
# correct place, so "2" is our missing first postive number.

# driver test function
if __name__ == '__main__':
    arr = [3, 4, 7, 1]
    print(compute_missing(arr))
