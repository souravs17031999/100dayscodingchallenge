# Program for computing count of all inversions of array - inversions are all such pairs (i, j) s.t. i < j and arr[i] < arr[j]
# IDEA: Logic is to compute on idea of merge sort algorithm, we can observe merge sort inherently compares both the subarrays divided recursively,
# and so, we can count of inversion while merging the arrays
# What we do is we recursively try to divide the array until only one element is left, where inversion is 0 (base case), and then merge it and count the
# inversions while merging.
# In this way, we are dividing, conquering and then combining our solutions to the overall problem.
# TIME : 0(n*lg(n)), SPACE : 0(n)


# function for merging subrouting and counting inversions
def merge(arr, left, mid, right):
    # print(f"going for merging, left : {arr[left:mid]} right : {arr[mid:right]}")
    i, j = left, mid + 1
    k = left
    temp_arr = [0] * 1000000
    inv_count = 0
    # looping over the both the arrays
    while(i <= mid and j <= right):
        # if first array element is smaller
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        # if second array element is smaller
        else:
            # NOTE : THIS IS THE ONLY PART WHERE INVERSIONS WILL BE ADDED,
            # AS when we copy element from right array, then we know that elements
            # after left array element will always be greater than left chosen element when comparing with right
            # element, and so we can directly add (overall length of first array - current element + 1)
            inv_count += (mid - i) + 1
            temp_arr[k] = arr[j]
            j += 1
        k += 1
    # executes copying if remaining elements are from array 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    # executes copying if remaining elements are from array 2
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

# function to recursively divide the array
def compute_inversions(arr, left, right):
    # base case
    if left >= right:
        return 0

    mid = (left + right) // 2
    # print(f"mid : {mid}")
    # x computes inversions in left subarrays
    x = compute_inversions(arr, left, mid)
    # y computes inversions in right subarrays
    y = compute_inversions(arr, mid + 1, right)
    # z computes inversions for cross inversion
    z = merge(arr, left, mid, right)
    # print(x, y, z)
    return x + y + z

if __name__ == '__main__':
    arr = [1, 5, 2, 6, 3, 0]
    n = len(arr)
    print(f"No.of inversions : {compute_inversions(arr, 0, n - 1)}")
