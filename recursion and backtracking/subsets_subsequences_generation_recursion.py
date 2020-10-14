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

# If we want to generate subsequences, then simply ignore empty subset.

def subsequence(arr, index, subset):
    if len(subset) != 0:
        print(subset)
    for i in range(index, len(arr)):
        subset.append(arr[i])
        subsequence(arr, i + 1, subset)
        subset.pop()

arr = [1, 2, 3]
subsets(arr, 0, [])
arr = [1, 2, 3]
subsequence(arr, 0, [])
    
