# Program for zeros and ones segregatation, efficiently.
# Idea is to basically keep two pointers and then, we can keep on moving left pointers (incrementing) until we hit 1, and then keep on moving
# right pointers (decrementing) until we hit 0, and then, we will be able to actually stop at that position and now,
# if left < right, then it means that "1" is at left pointer, "0" is at right pointer, so we need to swap these both.
# In this way, all 0's will be at front, and then all 1's will be at back of the array.
# This is also efficient in a way such that only one pass is required otherwise we can also simply count the number of times "1" and "0" occurs
# and simply copy to the original array resulting in segregatation but that can take more than one pass.
# TIME : 0(N), SPACE : 0(1)

import random
def segregate(arr, n):
    left, right = 0, n - 1
    while left < right:

        while arr[left] == 0 and left < right:
            left += 1

        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = 0, 1
            left += 1
            right -= 1

    return arr

if __name__ == '__main__':
    arr = [random.randint(0, 1) for _ in range(10)]
    print(arr)
    segregate(arr, len(arr))
    print(arr)
