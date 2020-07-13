# Program to search in sorted rotated array
# IDEA: Firstly we can either directly search the array using linear search in 0(N) but that is inefficient,
# and also we can't use direct normal binary search as this array is not only sorted but also rotated so indices positions will change.
# We have to use some modified use of binary search but we have to use it since array is sorted and can be sorted in 0(lg(N)).
# Finally, using rotated concept, we can use this fact to solve this using the fact that if arr[mid] is less than high pointer, then this means
# the high pointer is unchanged in binary search so, it means this right half is sorted and then we can check if element is actually in this space.
# Or if arr[mid] is greater than low pointer, then that means left segment (lower half) is sorted, so, this means we can check if actually
# the element is present in this space or not.
# TIME : 0(lg(N)), space : 0(1)

def search_rotate(arr, key):
    # setting initial pointers
    low, high = 0, len(arr) - 1
    while low <= high:

        # middle will finally return the searched element
        mid = (low + high) // 2

        # find the pivot element between the segments
        if arr[mid] == key:
            return mid

        # this means that right half is sorted arr[mid....high]
        elif arr[mid] <= high:
            if arr[mid] < key <= high:
                low = mid + 1
            else:
                high = mid - 1
        # this means that left half is sorted arr[low...mids]
        else:
            if low <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1


# driver function
if __name__ == '__main__':
    arr1 = [3, 6, 8, 9, 12, 14, 18, 21]
    arr2 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    print(search_rotate(arr1, 14))
    print(search_rotate(arr2, 6))
