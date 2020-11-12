# Program for computing max-path sum from any node to any node for a given binary tree.
# Logic is to solve using DP approach => 
# TIME : 0(N)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys 
class Solution:
    
    def max_path(self, root, res):
        
        if root == None:
            return 0
        
        left = self.max_path(root.left, res)
        right = self.max_path(root.right, res)
        
        temp = max(max(left, right) + root.val, root.val)
        ans = max(temp, left + right + root.val)
        
        res[0] = max(res[0], ans)
        
        return temp
        
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        res = [-sys.maxsize-1]
        self.max_path(root, res)
        return res[0]
