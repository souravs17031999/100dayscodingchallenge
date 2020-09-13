# Program for sorting the array using reverse function(arr, i, j).
# This is called pan-cake sorting.

# [3, 2, 4, 1]  => [1, 2, 3, 4]
#
# * reverse(arr, i, j)
#
# reverse(0, 2) => [4, 2, 3, 1]
# reverse(0, 3) => [1, 3, 2, 4]
# reverse(0, 1) => [3, 1, 2, 4]
# reverse(0, 2) => [2, 1, 3, 4]
# reverse(0, 0) => [2, 1, 3, 4]
# reverse(0, 1) => [1, 2, 3, 4]
#
# Idea is to one by one simply place the elements at its correct position, and for that we need to go for max element
# one by one.
# Let's say, we move max element "4" from its position to beginning, and then reversing the entire array will move it to last.
# [1, 3, 2, 4]
# Now, one element that is max element, is at its correct position.
# Then, we move to next max element "3" and move it to first index again by reversing till that found position, and then
# finally again reverse the array till size - 1, as one element is already sorted.
# [2, 1, 3, 4]
# Now, two elements are correctly placed.
# Similarly, going for "2", we reverse and then again reverse for size-2, giving [1, 2, 3, 4]
# Finally, array is sorted.

# ------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N ^ 2)
# SPACE : 0(N), # ONLY IF OUTPUT IS REQUIRED 

import sys

def reverse(arr, left, right):

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def find_max(arr, n):
    max_idx, max_ele = None, -sys.maxsize-1
    for i in range(n):
        if arr[i] > max_ele:
            max_idx = i
            max_ele = arr[i]
    return max_idx

def pancake_sort(arr, n):

    if not arr:
        return

    curr_size = n
    res = []  # contains all the flips (reverse) we do
    while curr_size > 1:
        max_idx = find_max(arr, curr_size)

        if max_idx != curr_size - 1:
            reverse(arr, 0, max_idx)
            reverse(arr, 0, curr_size-1)

            res.append(max_idx + 1)  # in actually, its max_idx but since in LC, we assumed 1-based indexing
            res.append(curr_size) # similarly like aboev, curr_size - 1
        curr_size -= 1

    return res

if __name__ == '__main__':
    arr = [3, 2, 4, 1]
    print(arr)
    print(pancake_sort(arr, len(arr)))
    print(arr)
