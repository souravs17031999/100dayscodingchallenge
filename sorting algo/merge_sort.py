def Merge(arr, left, mid, right):
    temp_arr = [0] * (right - left + 1)
    print(temp_arr)
    i, j = left, mid + 1
    k = left
    # looping over the both the arrays
    while(i <= mid and j <= right):
        # if first array element is smaller
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        # if second array element is smaller
        else:
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
        temp_arr[k] = temp_arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]


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
