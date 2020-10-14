# Program to print all the combinations (subsets) which sum up to given number N.
# Constrainst : 
# 1 <= candidates.length <= 30
# All elements of candidates are distinct.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
# So, exponential time complexity solution is also valid according to given constrainst.
# ------------------------------------------------------------------------------------------------------------------------------------
# We simply follow the same approach as we did in generating all the subsets but now there will be just few minor changes, and that will be that we are now allowed to use 
# the same number unlimited number of times, hence we now call the same number also in the recursive call.
# Also, we will now have additional parameter called target and use it to define our base case to stop this recursion using the idea that we will keep subtracting target 
# from our currently added item/element.
#                                 
#                              ([],0,7)    
#                                /   \
#                             [2],0,5    
#                             /  \
#                    [2,2],0,3  
#                  /   |     |  \
#      [2,2,2],0,3 [2,2,7],3,-4 [2,2,6],2,-3 [2,2,3],1,0   => answer
#       /
#    [2,2,2],0,1
#    /            \                 \              \
#  [2,2,2,2],0,-1  [2,2,2,3],-2    [2,2,2,6],2,-5     [2,2,2,7],3,-6
#
#[] 0 7
#[2] 0 5
#[2, 2] 0 3
#[2, 2, 2] 0 1
#[2, 2, 2, 2] 0 -1
#[2, 2, 2, 3] 1 -2
#[2, 2, 2, 6] 2 -5
#[2, 2, 2, 7] 3 -6
#[2, 2, 3] 1 0
#[2, 2, 3]
#[2, 2, 6] 2 -3
#[2, 2, 7] 3 -4
#[2, 3] 1 2
#[2, 3, 3] 1 -1
#[2, 3, 6] 2 -4
#[2, 3, 7] 3 -5
#[2, 6] 2 -1
#[2, 7] 3 -2
#[3] 1 4
#[3, 3] 1 1
#[3, 3, 3] 1 -2
#[3, 3, 6] 2 -5
#[3, 3, 7] 3 -6
#[3, 6] 2 -2
#[3, 7] 3 -3
#[6] 2 1
#[6, 6] 2 -5
#[6, 7] 3 -6
#[7] 3 0
#[7]
# --------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    
    def combinations(self, subset, index, candidates, output, target):
        
        if target < 0:
            return 
        
        if target == 0:
            output.append(subset.copy())
            return 
    
        for i in range(index, len(candidates)):
            subset.append(candidates[i])
            self.combinations(subset, i, candidates, output, target - candidates[i])
            subset.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        self.combinations([], 0, candidates, output, target)
        return output
