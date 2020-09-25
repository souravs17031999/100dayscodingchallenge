# Program to search in sorted rotated array
# IDEA: Firstly we can either directly search the array using linear search in 0(N) but that is inefficient,
# and also we can't use direct normal binary search as this array is not only sorted but also rotated so indices positions will change.
# We have to use some modified use of binary search but we have to use it since array is sorted and can be sorted in 0(lg(N)).
# Finally, using rotated concept, we can use this fact to solve this using the fact that if arr[mid] is less than high pointer, then this means
# the high pointer is unchanged in binary search so, it means this right half is sorted and then we can check if element is actually in this space.
# Or if arr[mid] is greater than low pointer, then that means left segment (lower half) is sorted, so, this means we can check if actually
# the element is present in this space or not.
# TIME : 0(lg(N)), space : 0(1)

"""
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid - 1
            
            else:
                
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1


# driver function
if __name__ == '__main__':
    arr1 = [3, 6, 8, 9, 12, 14, 18, 21]
    arr2 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    print(search_rotate(arr1, 14))
    print(search_rotate(arr2, 6))
