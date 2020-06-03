import random
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def bucket_sort(x):
    # create buckets and initialize
    slot_num = 10
    arr = [[] for _ in range(slot_num)]
    # putting items into correct buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # sorting each buckets individually
    for i in range(len(arr)):
        arr[i] = insertion_sort(arr[i])
    # putting all the elements from buckets back into original array in sorted order 
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
    return x


if __name__ == '__main__':
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"unsorted array : {arr}")
    print(bucket_sort(f"sorted array : {bucket_sort(arr)}"))
