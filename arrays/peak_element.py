# program to find the index of peak element - that is the element which is greater than either of the side elements (including boundary elements)

# IDEA: logic is to use binary search approach , as if the element we are at is lesser than left element then peak element is on left half otherwise right half , if current element is not the peak element.
# now, we can apply binary search method (divide and conquer) and narrow down our search

# this will work only if given that boundary elements are lower than each of other element otherwise a slight modification is needed when we will be considering corner cases by just changing if condition little bit

# importing sys module to make I/O faster 
import sys
def peak_element(arr, start, end, n):
    # here we are iterating till both start and end collides
    while(start <= end):
        # calculating middle element
        mid =  start + (end - start) // 2
        # if middle found is greater than its left and right one , then return this index , here if we are given that we have to include boundary elements also, then we just need to modify this line as (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])
        if arr[mid - 1] <= arr[mid] and arr[mid + 1] <= arr[mid]:
            return mid
        # if middle found is lessser than the left element  then simply, search on the left half
        elif arr[mid] < arr[mid - 1]:
            end = mid - 1
        # otherwise, peak element is on right half
        else:
            start = mid + 1


# main function
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(arr)
    print(peak_element(arr, 0, n-1, n))
