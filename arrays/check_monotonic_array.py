# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Example 1:
#
# Input: [1,2,2,3]
# Output: true
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
# Example 3:
#
# Input: [1,3,2]
# Output: false
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
# Example 5:
#
# Input: [1,1,1]
# Output: true
# -----------------------------------------------------------------------------------------------------------------------------------------------
# According to definition above we know that if either of the above condition is true that is either monotonically increasing or monotonically decreasing, the array 
# is considered to be monotonic otherwise not which is what is implemented below.
# ----------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N) , SPACE : 0(1)
#
# Follow up : Can you do it in one pass ?

# Without follow up : 
class Solution:
    def is_increasing(self, arr, N):
        
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                return False
        
        return True
    
    def is_decreasing(self, arr, N):
        
        for i in range(N - 1):
            if arr[i] < arr[i + 1]:
                return False
        
        return True
        
    def isMonotonic(self, A: List[int]) -> bool:
        
        N = len(A)
        if not N:
            return False 
        
        if N == 1:
            return True
        
        if self.is_increasing(A, N) or self.is_decreasing(A, N):
            return True 
        
        return False
    
# follow up : 

def isMonotonic(self, A: List[int]) -> bool:

    N = len(A)
    if not N:
        return False 

    if N == 1:
        return True

    increasing = decreasing = True
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            increasing = False 
        elif A[i] < A[i + 1]:
            decreasing = False 

    return increasing or decreasing
