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

# ------------------------------ More clear and concise using two pointer method , one at first and another at last --------------------------------------------------------
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        temp = [None] * len(A)
        left, right = 0, -1
        idx = len(A) - 1
        while idx >= 0:
            if A[left] * A[left] >= A[right] * A[right]:
                temp[idx] = A[left] * A[left]
                left += 1
            else:
                temp[idx] = A[right] * A[right]
                right -= 1
            
            idx -= 1
        
        return temp
    
 
# -------------------------------- More transformation equation applied to each applied : a * (x ** 2) + b * (x) + c ----------------------------------------------------
f = lambda  x, a, b, c : a * (x ** 2) + b * (x) + c

def sort_transform(arr, a, b, c, N):
    
    left, right = 0, N - 1
    temp = [None] * N
    idx = N - 1 if a >= 0 else 0
    
    while left <= right:
        l, r = f(arr[left], a, b, c), f(arr[right], a, b, c)
        if a >= 0:
            if l >= r:
                temp[idx] = l
                idx -= 1
                left += 1
            else:
                temp[idx] = r
                idx -= 1
                right -= 1
        
        else:
            if l >= r:
                temp[idx] = r
                idx += 1
                right -= 1
            else:
                temp[idx] = l
                idx += 1
                left += 1
            
    
    return temp


if __name__ == '__main__':
    assert sorted_square([-9, -2, 0, 2, 3], 5) == [0, 4, 4, 9, 81]
    assert sorted_square([-4, -1, 0, 3, 10], 5) == [0, 1, 9, 16, 100]
    assert sorted_square([-7, -3, 2, 3, 11], 5) == [4, 9, 9, 49, 121]
