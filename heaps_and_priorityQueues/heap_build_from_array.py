# Program to build a binary heap from given array
# Idea is to maintain the property of heap everytime we start building the max- heap that is any node in the heap should be greater than either
# of its two child nodes (if they exist)
# So, it is observed that for a node to be heapified, we need to ensure that its children are also heapified .
# It means we need to build the heap in bottom up order and also in any binary heap, below n//2 levels, we have all child nodes and so they are already
# heapified.
# Hence, we can simply start from index(n//2 - 1) till index(0), and for every index, we call heapify recursively to maintain heap property
# at each point.
# Heapify takes (0(lg(n))) time.
# BuildHeap takes average 0(n*lg(n)) but its runtime execution is found to be practically 0(N).

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


# driver test function
if __name__ == '__main__':
    arr = [4, 10, 3, 5, 1]
    BuildHeap(arr, 5)
    print(arr)
