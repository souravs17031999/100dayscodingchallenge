# Program taking input of sorted list of negative and positive numbers, and we need to
# give the output: squares of numbers in the sorted order.

# So, first of all, what is the form of output we need to return ? so, let's assume we can
# return a newly created list of sorted squares of the input list.
# Naive approach would be to simply square the numbers and apply in-built sort ,
# that will take time : 0(N*lg(N)) with 0(1) space.
# Can we optimize it more ?
# We can square the numbers up and then use Counting sort on this array.
# This will take, time : 0(N), space : 0(max(arr)).
# Now, can we optimize it further in terms of space efficiency ?
# So, we need to observe and use the inherent property that given array is already sorted.
# So, we can simply think about a partition, which can divide the array into positive and
# negative parts of array.
# Then, we can apply merge procedure for two sorted parts - one contaning all of positive
# and one contaning all of negative.
# This will Take TIME : 0(N), SPACE : 0(N), N IS SIZE OF ARRAY.

def sorted_square(arr, n):
    k = 0
    for k in range(n):
        if arr[k] >= 0:
            break

    i, j, ind = k - 1, k, 0

    temp = [0] * n
    while i >= 0 and j <= n - 1:
        if arr[i] * arr[i] < arr[j] * arr[j]:
            temp[ind] = arr[i] * arr[i]
            i -= 1
        else:
            temp[ind] = arr[j] * arr[j]
            j += 1

        ind += 1

    while i >= 0:

        temp[ind] = arr[i] * arr[i]
        i -= 1
        ind += 1

    while j <= n - 1:

        temp[ind] = arr[j] * arr[j]
        j += 1
        ind += 1

    return temp

if __name__ == '__main__':
    assert sorted_square([-9, -2, 0, 2, 3], 5) == [0, 4, 4, 9, 81]
    assert sorted_square([-4, -1, 0, 3, 10], 5) == [0, 1, 9, 16, 100]
    assert sorted_square([-7, -3, 2, 3, 11], 5) == [4, 9, 9, 49, 121]
