# Program to compute and return the pivot for the sorted rotated array, where pivot is simple the peak
# element which is greater than its next element and divides the array into two monotonically increasing
# halves.
# IDEA: Naive solution is to basically check if there is any element that it;s next is lesser than the current , because we can only have
# just one peak element which will also divide both the half arrays into increasing halves.
# Looping over and checking : if arr[i] > arr[i + 1]: return i , all this in 0(N) without using any extra space.
# can we do better ? can we use the property of sorted inherent order ?
# Yes, we can use actually binary search because of the sorted order and when we get mid, then maybe that will be the pivot element,
# or maybe not, so, there may be that mid will divide the array into two parts (if that is not pivoted), then one part will be sorted
# and other part non sorted, then our pivot will be contained in unsorted part of array, so we can continue our binary search in that part.
# We can also check by drawing diagram (graph) :
#-------------------------------------------
#   /|    /
#  / |  /
# /  | /
#/   |
#--------------------------------------------
# TIME : log(N) N is size of array.

def find_pivot(arr, n):

    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        elif mid < n and arr[mid] > arr[mid + 1]:
            return mid
        else:
            if arr[start] >= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

if __name__ == '__main__':
    arr, n = [2, 3, 4, 5, 6, 7, 8, 1], 8
    print(find_pivot(arr, n))
