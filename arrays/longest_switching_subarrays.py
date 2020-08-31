# program for computing the length of longest switching subarrays.
# An array is called "switching" if the odd and even elements are equal.
# EX.
# [2, 4, 2, 4] : the members in even positions (indexes 0 and 2) and odd positions (indexes 1 and 3) are equal.
# If A = [3,7,3,7, 2, 1, 2], the switching sub-arrays are:
# == > [3,7,3,7] and [2,1,2]
#
# Therefore, the longest switching sub-array is [3,7,3,7] with length = 4.
#
# As another example if A = [1,5,6,0,1,0], the the only switching sub-array is [0,1,0].
#
# Another example: A= [7,-5,-5,-5,7,-1,7], the switching sub-arrays are [7,-1,7] and [-5,-5,-5].
# ------------------------------------------------------------------------------------------------------------------------
# Here, naive solution would be to generate all substrings and then check if it is switching and get the max length.
# It would take 0(N^3) which is not good, so can we do better ?
# Actually, we can use sliding window technique here to get the max length.
# We know already that if there are only 2 elements then it is always switching, and then we start from 2nd index,
# and keep checking if the next element makes our subarray so far switching or not, depending on it, we either increment the temp length obtained
# so far or we simply initiliaze it back again to 2.
# We keep updating the max found so far.
# TIME : 0(N)


def compute_longest_switching(arr):

    n = len(arr)
    if n <= 2:
        return n

    count = 2
    temp = 2
    for i in range(2, n):
        if arr[i] == arr[i - 2]:
            temp += 1
        else:
            temp = 2

        count = max(count, temp)

    return count

arr = [3,7,3,7, 2, 1, 2]
print(compute_longest_switching(arr))
print(compute_longest_switching([7,-5,-5,-5,7,-1,7]))
