# Program for checking if given array forms binary heap or not.
# idea is to check from last internal node that is at n//2  - 1 , to check
# if at any node up the tree, we have if any voilation of heapify depending on
# whether we are checking min-heap, or max-heap.
# TIME : 0(N), space : 0(1).

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 1

def Check_Heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):

        if arr[i] < arr[left(i)]:
            return False

        if arr[i] < arr[right(i)]:
            return False

    return True


if __name__ == '__main__':
    arr = [90, 15, 10, 7, 12, 2]
    print(Check_Heap(arr))
    arr1 = [90, 15, 10, 7, 12, 2, 7, 3]
    print(Check_Heap(arr1))
