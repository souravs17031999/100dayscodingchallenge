# program to merge two sorted array together and return the sorted array
# Method 1 efficient is to simply create a additional third array to keep the sorted elements, now create three pointers each one for all three arrays,
# now, check whichever is small, copy that element in the third array and then simply increment that array's pointer , similarly when one of the
# pointer exhausts due to array size, start simply copying them one by one as they are already sorted within themselves.
# time : 0(m + n)
# space : 0(m + n)

def merge(arr1, arr2):
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    if arr1_size == 0:
        return arr2
    if arr2_size == 0:
        return arr1
    # third array for returning sorted elements
    arr3 = [0] * (arr1_size + arr2_size)
    i, j, k = 0, 0, 0
    # looping over the both the arrays
    while(i < arr1_size and j < arr2_size):
        # if first array element is smaller
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        # if second array element is smaller
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    # executes copying if remaining elements are from array 1
    while i < arr1_size:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    # executes copying if remaining elements are from array 2
    while j < arr2_size:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    return arr3

# Method 2 focuses on without using any additional space
# idea is to simply pick the elementes one by one from last of second array, and start traversing from last of first array
# and then, keep on shifting the elements right one by one until we found a postion for second elemetn in the first array,
#  in which case then, we have to swap the elements in both arrays, threby maintaining sorted order.
# time : 0(m*n)
# space : 0(1)

def merge_mod(arr1, arr2):
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    if arr1_size == 0:
        return
    if arr2_size == 0:
        return
    # looping from back of second array
    for i in range(arr2_size - 1, -1, -1):
        # setting pointer for first array
        j = arr1_size - 2
        # saving the last element
        last = arr1[arr1_size - 1]
        # looping over the first array and shifting the elements
        while j >= 0 and arr2[i] < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        # now, the position is found, then just putting elements in appropriate positions
        if j != arr1_size - 2 and last > arr2[i]:
            arr1[j + 1] = arr2[i]
            # everytime last will change, as arr1 is modified
            arr2[i] = last



# main driver function

if __name__ == '__main__':
    assert merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]) == [1, 2, 3, 5, 8, 9, 10, 13, 15, 20]
    assert merge([], [2, 3, 8, 13]) == [2, 3, 8, 13]
    assert merge([1, 5, 9, 10, 15, 20], []) == [1, 5, 9, 10, 15, 20]
    assert merge([1, 5, 9, 9, 10, 15, 20, 20, 20], [2, 3, 8, 8, 10, 10, 13, 13]) == [1, 2, 3, 5, 8, 8, 9, 9, 10, 10, 10, 13, 13, 15, 20, 20, 20]
