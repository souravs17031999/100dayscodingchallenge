
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# Given following is a description : 
# suppose the array : [0,1,0,2,1,0,1,3,2,1,2,1]
# 
#                                 ____
#               ____ ++++    +++ |   |____    ___
#      ____    |   | ___     ____|       |_++|   |___
#    __|___|++_|___ ____|_++|___ ___ ___ __|____ ___|____
#
# ++ shows rain water area blocks.
# || shows heights/elvation as given in the array.
#
# Total area : 0 + 1 + 0 + 1 + 2 + 1 + 0 + 0 + 1 + 0  + 0 = 6 (3 of area 1 * 1, 1 of area 3 * 1)

# ------------------------ Approach/ intuition ----------------------------------------------------------------------------------------------------------

# Here, we need to first observe that water trapped is only bounded by the heights of the left and right buildings which are maximum in either direction.
# We can easily visualize it and verify.
#                                              _____
#     ____                                     |    |
#    |    |         ⬆️                        |    |
#    |    |          +                         |    |
#    |    |          +   *  -----              |    |
#    |    |          +   * |    |              |    |
#    |    |          +   * |    |              |    |
#    |____|.........⬇️..*.|____|..............| ___|
#
# We can easily verify from above at middle building, that water level is given by min(max value from left buildings, max value from right buidings) - height of current building
# water level  = {<+++++>} - {****} => this will tell us the height of the buildings.
# Now, this way we get all the water levels at every element and sum them up to get total area.

# Naive solution in 0(N^2)

# class Solution:
#    def trap(self, height: List[int]) -> int:
#       
#        if len(height) == 0 or len(height) == 1:
#            return 0
#       
#        rain_area = 0
#        for i in range(1, len(height)-1):
#
#            max_val_left = height[i]
#            for j in range(0, i):
#                max_val_left = max(max_val_left, height[j])
#
#            max_val_right = height[i]
#            for j in range(i + 1, len(height)):
#                max_val_right = max(max_val_right, height[j])
#
#            rain_area += (min(max_val_left, max_val_right) - height[i])
#
#        return rain_area
#
# ------------------------------------------------------------------- efficient solution in time : 0(N), space : 0(N) ---------------------------------------------------------
#
# Now, we can actually construct two different arrays left_height[] and right_height[] so that this preprocessing can help to reduce this time complexity.
# we can get all the max left heights for all the elements one by one by comparing the current height with last max left value height filling from left to right.
# Similarly, we can get all the max right heights for all the elements one by one by comparing the current height with last max right value height filling from right to left.
# Then, water level = min(left_height[i], right_height[i]) - height[i]
# Hence, we can sum up all the water levels for all the buildings.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0 or len(height) == 1:
            return 0
        
        rain_area = 0
        left_height, right_height = [-sys.maxsize-1] * len(height), [-sys.maxsize-1] * len(height)

        left_height[0] = height[0]
        for i in range(1, len(height)):
            left_height[i] = max(left_height[i - 1], height[i])

        right_height[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_height[i] = max(right_height[i + 1], height[i])

        for i in range(len(height)):
            rain_area += (min(left_height[i], right_height[i]) - height[i])

        return rain_area

