def Merge(arr, l, m, r):
    arr1 = arr[l:m]
    arr2 = arr[m:r]

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


def MergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        MergeSort(arr, l, m)
        MergeSort(arr, m + 1, r)

        Merge(arr, l, m, r)

if __name__ == '__main__':
    arr = [1, 5, 9, 10, 15, 20, 2, 3, 8, 13]
    MergeSort(arr, 0, len(arr) - 1)
    print(arr)
