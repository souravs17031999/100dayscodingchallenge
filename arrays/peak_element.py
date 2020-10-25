# program to find the index of peak element - that is the element which is greater than either of the side elements (including boundary elements)
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#             or index number 5 where the peak element is 6.
#
# IDEA: Naive approach will be to iterate one by one for every element and check for its neighbours, it may happen that multiple peaks are found, but we can return anyone of them.
# It will take 0(N) time with space:  0(1), 
# Can we improve this solution ?
# logic is to use binary search approach , as if the element we are at is lesser than left element then peak element is on left half otherwise right half , if current element is not the peak element.
# now, we can apply binary search method (divide and conquer) and narrow down our search  
# this will work only if given that boundary elements are lower than each of other element otherwise a slight modification is needed when we will be considering corner cases by just changing if condition little bit
# Intuition is based on "promising_search_space" concept, as the array is not sorted so we can't compare directly with any key, but we can get some idea based on some conditions
# which half space can get us the required answer.   
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# TIME: LINEAR TIME 0(N) APPROACH : 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pos = 0
        n = len(nums)
        
        if n <= 1: return 0    
        if n == 2:
            if nums[0] > nums[1]: return 0
            if nums[1] > nums[0]: return 1
        
        if nums[0] > nums[1]: return 0
        
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                pos = i
                break
        
        if nums[n - 1] > nums[n - 2]: return n - 1 
        else: return pos

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# FOLLOW UP - LOGARITHMIC TIME COMPLEXITY ?        
        
# importing sys module to make I/O faster 
import sys
def peak_element(arr, start, end, n):
    # here we are iterating till both start and end collides
    
    n = len(nums)
    start, end = 0, n - 1
        
    # base cases    
    if n <= 1: return 0
    while(start <= end):
        # calculating middle element
        mid =  start + (end - start) // 2
        # if middle found is greater than its left and right one , then return this index , here if we are given that we have to include boundary elements also, then we just need to modify this line as (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])
        if mid > 0 and mid < n - 1:
            
            if nums[mid - 1] <= nums[mid] and nums[mid + 1] <= nums[mid]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid - 1
            else:
                start = mid + 1
        
        # handling corner cases 
        # for very first element 
        elif mid == 0:
            if nums[0] > nums[1]: return 0
            else: return 1
        # for very last element     
        elif mid == n-1:
            if nums[n-1] > nums[n-2]: return n-1
            else: return n-2
        
        


# main function
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(arr)
    print(peak_element(arr, 0, n-1, n))
