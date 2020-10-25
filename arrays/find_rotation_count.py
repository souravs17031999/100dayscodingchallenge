# Program for counting the rotation count of rotating the sorted array.
# The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
# Examples:
#
# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be 
# {2, 3, 6, 12, 15, 18}. We get the given array after 
# rotating the initial array twice.
#
# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4
#
# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# If we write the exlpicitly examples, then we can observe that k is equal to minimum value index in the array.
# arr : [2, 3, 6, 12, 15, 18]
# k = 1: [18, 2, 3, 6, 12, 15]
# k = 2: [15, 18, 2, 3, 6, 12]
# k = 3: [12, 15, 18, 2, 3, 6]
# Since, "2" is the minimum element which is also first element and since we are rotating it k times, so this element "min-value" will also rotate exactly k times, 
# and hence, the final index of this element is the value of "K".
# So, we can simply get the index of min value in 0(N).
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Now, can we do better than linear scanning ?
# Yes, using binary search to find this above shown index of min value.
# Using observations : 
# we can see that this min-value (mid) should be lesser than both of its neighbours, as it is the minimum element of the array, no other element would have this property.
# secondly, we can also see our min value when rotated, is either in left or right half, and that too it's in unsorted part of array.
# So, we can simply check if either half is unsorted , then move to that half space because that may contain our min value element.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(log(N)), SPACE : 0(1)

def count_rotations(arr):
    n = len(arr)
    start, end = 0, n - 1
    
    while start <= end:
    
        mid = start + (end - start) // 2
        prev, next = (mid + n - 1) % n, (mid + 1) % n  # since array is rotated, so considering edge cases into this so that last index next is first, and first prev is last ele
        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid 
        elif arr[start] <= arr[mid]:  # it checks whether left half is sorted, and so move to right half 
            start = mid + 1
        # otherwise move to right half     
        else:   
            end = mid - 1

print(count_rotations([15, 18, 2, 3, 6, 12]))
        
