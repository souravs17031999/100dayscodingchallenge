# Program for generating and printing all combinations of size "r".
# Approach will be to fix one one element at its position, and then either it will choose the current element or not choose the current element
# same as the one for subset/subsequence generation.
# Following is recursion tree visualized  :
#                    (0,0)
#                  /         \
#             (1,1)          (0,1)
#           /    \              /   \
#       (2,2)    (1,2)         (1,1) (0,2)
#       /\          /      \           
#   (3,3) (2,3)   (2,3)     (1,3)  
#          /\         /\          / \        /  (1,5)
#        (3,4) (2,4) (3,4) (2,4) (2,4) (1,4) \  (2,5)
#               /\          / \      / \   
#         (3,5) (2,5) (3,5) (2,5) (3,5) (2,5)
#
# ----------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(2 ^ n) tighter upper bound whereas upper bound can be 0(nCr).

arr = [1, 2, 3, 4, 5]

def combinations(arr, n, r, index, temp, i):
    
    if index == r:
        print(temp)
        return
    
    if i >= n:
        return
    
    temp[index] = arr[i]
    combinations(arr, n, r, index + 1, temp, i + 1)
    combinations(arr, n, r, index, temp, i + 1)

temp = [0] * 3
combinations(arr, 5, 3, 0, temp, 0)
