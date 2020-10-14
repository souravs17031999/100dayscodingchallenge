# Program for subset/subsequence generation using recursion + backtracking.
# Although this method is inefficient, as TIME : 0(2^n), exponential time.
# Approach is to simply think intuitively at every index of element, we have two choices either to take that element , or to not take that element.
# So, we go over all index, we include the current element, then again recurse for next set of array, then after finsihing this call, we again remove the current element 
# to backtrack to previous state, and include next element.
# Following recursion tree visualized :                
#   
#             [], 0
#           /   |   \
#         [1],1 [2],2  [3], 3
#       /   \        |
#   [1,2],2 [1,3],3 [2,3],3
#      |
#   [1,2,3],3
# ---------------------------------------------------------------------------------
# TIME : 0(2 ^ (N) * N) 

def subsets(arr, index, subset):
    print(subset)
    for i in range(index, len(arr)):
        subset.append(arr[i])
        subsets(arr, i + 1, subset)
        subset.pop()

# If duplicates also occur in array, then we need to skip those for distinct subsets: 
# Using sets for not counting those which are already generated.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        visited = set()
        n = len(nums)
        nums.sort()
        for i in range(2 ** n):
            temp = []
            for j in range(0, n):
                if i & (1<<j):
                    temp.append(nums[j])
            
            if tuple(temp) not in visited:
                output.append(temp)
                visited.add(tuple(temp))
        
        return output

arr = [1, 2, 3]
subsets(arr, 0, [])
arr = [1, 2, 3]
subsequence(arr, 0, [])
    
