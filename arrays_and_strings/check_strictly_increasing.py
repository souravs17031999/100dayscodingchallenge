# Program to check if array is non-decreasing, that means in the array for all n, nums[i] <= nums[i + 1].
# IDEA: logic is to bascially check for every nums[i], if we anywhere we voilate above property, then we can simply replace that element
# by mid of both (left and right element), which will ensure the replaced element is correctly greater than previous one and lesser than
# after element which goes with the definition of increasing array.
# Also, we can check separately for first element and last element.
# Also, we count all modifications, if greater than 1, then we return False otherwise True.
# TIME : 0(N), SPACE : 0(1).

from sys import stdin, stdout
import random

def check_Increasing(arr):
    n = len(arr)
    count = 0
    # if empty list, then return False
    if not n:
        return False

    # if singleton list, then obviously true
    if n == 1:
        return True

    # if atleast lenght 2, then we need to check separately for first place element if any
    # modification is needed
    if n >= 2:
        if arr[0] > arr[1]:
            arr[0] = arr[1] // 2
            count += 1

    # for other elements, only two cases arise when there is any modification needed
    for i in range(1, n - 1):
        if (arr[i - 1] < arr[i] and arr[i] > arr[i + 1]) or (arr[i - 1] > arr[i] and arr[i] < arr[i + 1]):
            arr[i] = (arr[i - 1] + arr[i + 1]) // 2
            count += 1

            if (arr[i] == arr[i - 1] or arr[i] == arr[i + 1]):
                return False

    # if atleast lenght 2, then we need to check separately for last place element if any
    # modification is needed
    if n >= 2:
        if arr[n - 2] > arr[n - 1]:
            count += 1

    if count > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    arr = [random.randint(0, 10) for _ in range(3)]
    arr = [3, 4, 2, 3]

    print(arr)
    print(check_Increasing(arr))
    print(arr)
