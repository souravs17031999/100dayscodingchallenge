# Porgram to implement heap sort using max - heap
# Heapify takes (0(lg(n))) time.
# BuildHeap takes average 0(n*lg(n)) but its runtime execution is found to be practically 0(N).
# Max-heap takes 0(n*lg(n)) time.
# This is in-place sorting untsable algorithm (but can be made stable).

def heapify(arr, n, i):
    # we initialize the largest to be current element (element to be swapped)
    largest = i
    left = 2 * i + 1  # extract left index
    right = 2 * i + 2 # extract right index

    # we compare the left child with the current element and set it largest if its maximum that current element
    if left < n and arr[left] > arr[i]:
        largest = left

    # now, since we are comparing the current maximum so far with the right child, hence we obtain overall maximum
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if there is a change in largest, it means there is voilation of heap property and we need to swap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # call heapify recursively for every node one by one top to down
        heapify(arr, n, largest)

# building heap from n//2 -1 till 0 (all levels except last level)
def BuildHeap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr, n):
    BuildHeap(arr, n)
    print(f"BuildHeap : {arr}")
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    print(f"sorted array : {arr}")

# driver test function
if __name__ == '__main__':
    arr = [4, 10, 3, 5, 1]
    print(f"Given array : {arr}")
    heapsort(arr, 5)
