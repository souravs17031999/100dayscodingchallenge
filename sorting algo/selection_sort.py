def selection_sort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__ == '__main__':
    arr = [-90, 121, 0, -60, 1000]
    selection_sort(arr, 5)
    print(arr)
