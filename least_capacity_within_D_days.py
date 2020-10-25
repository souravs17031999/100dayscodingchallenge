# A conveyor belt has packages that must be shipped from one port to another within D days.
# The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: 
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
#
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
# Example 2:
#
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation: 
# A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:
#
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation: 
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Here, observing from the question we can understand and find out the range of the answer, that at minimum it can be maximum weight from the array, 
# as atleast that much weight will be required to ship to conveyor belt.
# Now, similarly, maximum weight can be actually the sum of all weights of the array as in one day, we can ship all the items in one go at max.
# So, range of ans = (max_element_array, sum_of_array)
# Now, Brute force way of doing this would be to check for all values in this range if number of days is withing given D(total days requirement), then true otherwise false.
# But, that would take time : 0(N) * (Max - Min)
# Now, can we do better than this ?
# Yes, we can observe actually this range is sorted monotonically, and so we can apply binary search for the range above shown and time complexity can be reduced to 
# Time : 0(N) * (log(Max - min))
# Binary search can be here modified one as when we will be able to fit "mid" number of days within given D, that means we can do in more than mid also, it means we have to 
# move to left half of search space so as to minimize the number of days required, similary if we are not able to fit calculated "mid", then it means we have to 
# move to right half space of search space to try the next possible value.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Time : 0(N) * (log(Max - min)), space : 0(1)

import sys
class Solution:
    
    def capacity_done(self, weights, D, c):
        
        days = 1
        capacity = c
        for i in range(len(weights)):
            if capacity >= weights[i]:
                capacity -= weights[i]
            else:
                days += 1
                capacity = c - weights[i]
        
        if days <= D: return True
        else: return False
            
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        start = max(weights)
        end = sum(weights)
        ans = sys.maxsize
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if self.capacity_done(weights, D, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans
