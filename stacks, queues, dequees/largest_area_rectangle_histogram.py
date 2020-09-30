# Program to compute largest area of rectangle in histogram.
# -------------------------------------------------------------------
#  1  2    3    4   5    3  3  2
#                  ----
#              ----|  |
#         ---- |  |   |------
#      --|    |  |    |  |  |---
# --- |  |   |   |    |  |  |  |
# |__|___|___|___|___|___|__|__|
#
# Following is the given histogram, where max area is 15.
# arr = [1, 2, 3, 4, 5, 3, 3, 2], so these numbers are basically hostogram
# heights.
# Naive solution to implement would be to simply fix a outer loop pointer for
# every histogram, then run inner loop pointer starting from itself to last height.
# Now, we compute minimum possible height for every possible starting index denoted by outer loop, 
# and we compute area using hist[min_height] * (j - i + 1).
# ---------------------------------------------------------------------------
# Can we do better ?
# Yes, what we are going to do is to actually first fix the max variable as
# max height because that's the maximum possible area considering it's bar and assuming width of all bars same (and equal to 1).
# Now, let's see, we will iterate from left to right, and go on till we find
# next smaller height bar.
# Now, we can see we can form the rectangle, from the current index and go to left possible index which can encompass the entire area under all bars.
# We can compute this area and update max if needed.
# Now, after doing this for all this iterations, we also need to check if there are elements / bars left, then it should be also be calculated.
# Now, while we are extending leftwards, then we are only worried about the current whatisever is just till index is greater than or equal to, so
# probaly stack will do much better.
# We are only concerned with the top of stack, if initially stack is empty, then we will push the curren hist index into the stack, or if curren hist
# height is larger than top of stack, then simply push, if at any point , we find current hist index bar is smaller than top of stack, then we need to
# pop from top of stack, then we need to and calculate the area by computing as follow : area = hist[popped_index] * (right_idx - left_idx - 1) when stack
# is not empty, and if empty, then area = hist[popped_index] * (right_idx - 1)
# Now, after all this some values will be left in the index, then we need to
# pop it off and apply the small logic same as before and keep updating max.
# -----------------------------------------------------------------------------
# TIME : 0(N), space : 0(N).
# ----------------------------------------------------------------------------
# Naive approach in 0(N^2) : 
# import sys 
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
        
#         if len(heights) == 0:
#             return 0
        
#         if len(heights) == 1:
#             return heights[0]
        
#         max_area = -sys.maxsize-1
#         for i in range(len(heights)):
#             min_h = i
#             for j in range(i, len(heights)):
#                 if heights[j] <= heights[min_h]:
#                     min_h = j
#                 max_area = max(max_area, heights[min_h] * (j - i + 1))

#         return max_area

# Efficient solution : 

from collections import deque
def compute_histogram_area(hist):
    n = len(hist)
    max_area = max(hist)
    i = 0
    stack = deque()
    while i < n:

        if not stack or hist[stack[-1]] < hist[i]:
            stack.append(i)
            i += 1
        else:
            curr_max = stack.pop()
            area = hist[curr_max] * (i - stack[-1] - 1) if stack else i
            max_area = max(max_area, area)

    while stack:

        curr_max = stack.pop()
        area = hist[curr_max] * (i - stack[-1] - 1) if stack else i
        max_area = max(max_area, area)

    return max_area

hist = [6, 2, 5, 4, 5, 1, 6]
print("Maximum area is",  compute_histogram_area(hist))
hist = [1, 2, 3, 4, 5, 3, 3, 2]
print("Maximum area is",  compute_histogram_area(hist))
