# Program to find the bottom most left value in the binary tree.
# 
# Example 1:
# Input:
#
#    2
#   / \
#  1   3
#
# Output:
# 1
# Example 2:
# Input:
#
#        1
#       / \
#      2   3
#     /   / \
#    4   5   6
#       /
#      7
#
# Output:
# 7
# ------------------------------------------------------------------------------------------------------------------------------------
# Intuition is very simple here, we can simply see we have to go to the last level of binary tree and get the left most value in the last low of the tree.
# So, we go for BFS traversal level by level, but we need to go for right child first, then left child and so finally left most value is obtained at the last.
# ------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)
# ------------------------------------------------------------------------------------------------------------------------------------
# We can also go for DFS topdown traversal, and check for base case, if root is None, return, and one more important case if curr_level > level then we need to update 
# leftmost node value "ans" and also value of "level". Here, curr_level is current_row of binary tree, and level is last level so that as soon as our curr_level changes, 
# we need to get the leftmost node value and this goes for all the levels, so at last, we have left most value in the last row of binary tree.
# TIME : 0(N), SPACE : 0(N)
# ------------------------------------------------------------------------------------------------------------------------------------
# BFS APPROACH :

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque 
def findBottomLeftValue(root: Node) -> int:
    
    queue = deque()
    queue.append(root)
    curr = None
    
    while queue:
        
        curr = queue.popleft()
        print(curr.val, end = " ")
        if curr.right:
            queue.append(curr.right)
        if curr.left:
            queue.append(curr.left)

    return curr.val
    
# DFS APPROACH (TOPDOWN) : 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find_bottom(self, root, level, ans, curr_level):
    
        if root == None:
            return

        if curr_level > level[0]:
            level[0] = curr_level
            ans[0] = root.val

        self.find_bottom(root.left, level, ans, curr_level + 1)
        self.find_bottom(root.right, level, ans, curr_level + 1)
    
    
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        curr_level = 0
        level = [0]
        ans = [root.val]
        self.find_bottom(root, level, ans, curr_level)
        return ans[0]
