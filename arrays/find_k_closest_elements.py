# Program for computing the K closest elements for a given value in the array.
# Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. 
# The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
# ----------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
#
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
# ---------------------------------------------------------------------------------------------------------------------
# Naive solution will be to calculate asbsolute difference of all the elements, and then choose k closest elements.
# arr   : [1, 2, 3, 4, 5], and given k = 4, and x = 3
# diff  : [2, 1, 0, 1, 2]
# we choose 4 elements, [1, 2, 3, 4], here since, "2" difference repeats but we have to choose smallest element so, we ignore "5" and choose "1".
# make a pair of (diff, element) and sort it on basis of diff.
# then, take top k elements but this will take 0(N * log(N)).
# ----------------------------------------------------------------------------------------------------------------------
# Can we do better than this ?
# We can actually build the min-heap from the above made pair of tuples (diff, element).
# and then pop off k elements and return the result, but the problem is result should also be sorted and so it will again take 0(N * log(N) with space : 0(N).
# But if we don't want to sort the result, then we can do this in 0(N) time with 0(N) space.
# -----------------------------------------------------------------------------------------------------------------------
# Can we do more better than the above discussed approaches considering the inherent structure of the problem ? 
# Yes, if we observe the array is already sorted, then why to compute diff and sort it again (or use heap for that matter) ? 
# Can we apply some search technique which can help us to find the cross over point, the point before which elements are smaller than or equal to x and after 
# which greater than x ? Binary search can be useful tool for that.
# We first find that point , either it will be equal to that value only (equal to "x"), otheriwise it will be closest value found acc. to binary search.
# EX.     
#                                            
#                                     [1, 2, 3, 4, 5]
#                                            ^  ^
#                                            |  |
#                                           left right
#                                             
#
# Marked point is the cross over point, as actually closest element will be around this cross over point due to the fact that array is sorted, 
# when we move to right side, diff will be small at first but then start increasing, similarly, when we move to left side, diff will be small at first, but then start increasing
# so, this is actually type of concentric circles of radius of those "k" closest radii.
# So, we can know keep two pointers, left and right one at crossover and other one next to crosoover, and check simulatenously, which ever diff is smallest, then take that 
# and move that pointer accordingly, and also to take smallest one when diff equal include that also in the condition.
# TIME : 0(log(N) + K), space : 0(1) [only if sorting is not required in output order]
# ------------------------------------------------------------------------------------------------------------------------

# Heap based approach : 

from heapq import heapify, heappush, heappop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = [(abs(x - i), i) for i in arr]
        heapify(heap)
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        res.sort() # only required when submitting to leetcode
        return res

# Binary search based approach : 
class Solution:
    
    def cross_over(self, arr, x):
        
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end-start) // 2
            if arr[end] <= x:
                return end 
            
            if arr[start] > x:
                return start
            
            if arr[mid] <= x and arr[mid + 1] > x:
                return mid 
            if x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        count = 0
        n = len(arr)
        res = []
        
        if n <= 0: return []
        if n == 1: return [arr[0]]
        
        left = self.cross_over(arr, x)
        right = left + 1
        
        while left >= 0 and right < n and count < k:
            if x - arr[left] <= arr[right] - x:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            count += 1
        
        while count < k and left >= 0:
            res.append(arr[left])
            left -= 1
            count += 1
        
        while count < k and right < k:
            res.append(arr[right])
            right += 1
            count += 1
        
        res.sort() # only required when submitting to leetcode
        return res
            
        
