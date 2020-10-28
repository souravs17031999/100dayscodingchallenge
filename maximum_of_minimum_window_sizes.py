# Program for computing all maximums for all minimums of all the possible window sizes.
# Input: arr[] = {10, 20, 30, 50, 10, 70, 30}
# Output: 70, 30, 20, 10, 10, 10, 10
# The first element in the output indicates the maximum of minimums of all
# windows of size 1.
# Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10},
# {70} and {30}. Maximum of these minimums is 70
#
# The second element in the output indicates the maximum of minimums of all
# windows of size 2.
# Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10},
# and {30}. Maximum of these minimums is 30
# The third element in the output indicates the maximum of minimums of all
# windows of size 3.
# Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}.
# Maximum of these minimums is 20
#
# Similarly, other elements of output are computed.
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Brute force/naive approach would be to compute first minimum for all the possible window sizes, and then take maximum for all those minimum window size, 
# so, computing minimum would be done in 0(N * K) * N, and if we optimized it using sliding window + deque based approach, we can improve the computation of 
# minimum of window sizes to 0(N), and so overall it would be done in 0(N * N).
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Can we do more better than this ?
# Yes, actually, we can apply the logic same as we did in largest area of rectangle in histogram, it's a variation of same problem.
# So, we have to calculate left[] and right[] for computing NSL, NSR using stack as we have already seen.
# So, we have to compute right[i] - left[i] - 1, and calculate max of all of them.
# ------------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)

from collections import deque 

# computing nearest smallest to right
def NSR(arr, n, output):

    stack = deque()
    
    for i in range(n-1, -1, -1):  
        
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if not stack:
            output[i] = -1
        else:
            output[i] = stack[-1]
        
        stack.append(i)
    
# computing nearest smallest to left
def NSL(arr, n, output):

    stack = deque()
    
    for i in range(n):  
        
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if not stack:
            output[i] = -1
        else:
            output[i] = stack[-1]
        
        stack.append(i)
    

# computing max of min of all window sizes 
def max_min_subarray(arr):
    
    n = len(arr)
    ans = [0] * (n + 1)
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
    NSR(arr, n, right)
    NSL(arr, n, left)
    print(left)
    print(right)
    
    # window_length, which gives all window sizes, so, we have to fill that in position in arr
    for i in range(n):
        window_length = right[i] - left[i] - 1
        ans[window_length] = max(ans[window_length], arr[i])
    
    print(ans) # some entries are still "0" so, we are going to fill in with help of right side of ans 
    for i in range(n-1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    
    print()
    for i in range(1, n + 1):
        print(ans[i], end = " ")


arr = [10, 20, 30, 50, 10, 70, 30]  
n = len(arr) 
max_min_subarray(arr)
