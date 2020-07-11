from bisect import bisect_left

def bin_search(arr, key, start, end):
    index = bisect_left(arr, key, start, end)
    if index < end and arr[index]  == key:
        return index
    else:
        return -1

if __name__ == '__main__':
    arr = [1, 3, 5, 10, 100]  # the list must be already sorted before passing it to bisect.
    print(bin_search(arr, 10, 0, 4)) # 3
    print(bin_search(arr, 95, 0, 4)) # -1
