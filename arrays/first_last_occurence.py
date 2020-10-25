# Program to find first and last occurence of the sorted array.
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
# -------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
# --------------------------------------------------------------------------------------------------------
# Intuition is clearly due to being the array sorted we need to find the first and last position in the sorted array by using some kind of modified binary search
# so, we have to think how we can apply binary search to find the first and last pos.
# Now, if we get any position/occ in the array, then if we simply apply binary search then it will stop, so we don;t have to stop and keep searching for first/last occ., 
# and for that we need to move search space towards left for first occ, and move towards right for last occ.
# Let's say : [1, 2, 3, 3, 3, 4, 4, 5, 6], and target = 3, and so if we get "4" index as mid, and arr[4] = 3, but this is not occ, and so
# we move to left by moving end = mid - 1, then again 3 matches at index "3", but this is not also first occ, 
# and so again we move to left, at index "2", and keep saving the last matched position, after that loop finishes, 
# and we get answer as index "2".
# Similarly, for the last occurence of target in array.
# ---------------------------------------------------------------------------------------------------------

# TIME : 0(log(N)), SPACE : 0(1)

class Solution:
    
    def first_occurence(self, arr, key):
    
        start, end = 0, len(arr) - 1
        pos = -1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1

            elif key > arr[mid]:
                start = mid + 1

            else:
                pos = mid 
                end = mid - 1

        return pos

    def last_occurence(self, arr, key):

            start, end = 0, len(arr) - 1
            pos = -1
            while start <= end:
                mid = start + (end - start) // 2
                if key < arr[mid]:
                    end = mid - 1

                elif key > arr[mid]:
                    start = mid + 1

                else:
                    pos = mid 
                    start = mid + 1

            return pos
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first, last = self.first_occurence(nums, target), self.last_occurence(nums, target)
        return [first, last]
