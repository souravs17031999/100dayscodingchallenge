# Program for computing max product of subarrays for a given array
# Naive solution will be same as for max sum subarrays, in 0(N^3).
# Approach will be same, but there is trick here which also needs to be accounted for, and that is
# we know we are getting big number when taking positive number, and ignoring negative numbers, but the fact is that
# if our running product is -ve, and new number is also negative, then it maybe possible that overall product becomes bigger (as is positive)
# So, in addition to max_prod, we also need to keep a running min_prod which keeps minimum so far, and using both we will able to get
# max and keep updating overall max.
# ----------------------------------------------------------------------------------------------------------------------------------------
# EX. [-1, 6, 2, 3 ....]
# SO, LET'S SAY WE HAVE CALCULATED : IGNORING -1, 6 * 2 = 12, AND NEW NUMBER IS 3, THEN WE GET 12  * 3 = 36
# BUT EX. [-1, 6, 2, -2 ....]
# SO, LET'S SAY WE HAVE CALCULATED : IGNORING -1, max_prod = 12 AND AGAIN WE IGNORE -2, BUT THAT IS WRONG.
# AND HENCE, IF WE ALSO KEEP MIN_VALUE = -12 , THEN IT WILL TAKE INTO ACCOUNT : -12 * -2 = 24
# HENCE, OVERALL MAX IS 24 WHICH IS CORRECT FOR THIS CASE.
# ----------------------------------------------------------------------------------------------------------------------------------------
# SO, OVERALL WE CAN SAY :
# curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
# curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
# TIME: 0(N), SPACE : 0(1)

import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return
        curr_max, curr_min, max_prod = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(nums[i], max(curr_max * nums[i], curr_min * nums[i]))
            curr_min = min(nums[i], min(temp * nums[i], curr_min * nums[i]))
            max_prod = max(max_prod, curr_max)
        return max_prod
