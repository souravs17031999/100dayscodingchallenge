# Program to invert a binary tree.
# Meaning if we observe the below example, we will see that the inversion
# is a result of mirror image.
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# --------------------------------------------------------------------------------------------------

# We could think of building entirely new binary tree but that would be too inefficient and also it
# is not given by the question specifications.


# Most simple and efficient approach would be to simply as we can see we have to swap the left and
# right pointers relative to their root node, so we would go bottom up that is postorder traversal.
# First,we go left, then go right, after finish of traversal, we simply go for node processing where
# # simply we swap both left and right pointers.

# TIME : 0(N), N IS NUMBER OF NODES, SPACE : 0(N), AS WORST CASE RECURSION STACK (0(H)), H = 0(N)

# The idea is that we need to swap the left and right child of all nodes in the tree.
# So we create a queue to store nodes whose left and right child have not been swapped yet.
# Initially, only the root is in the queue. As long as the queue is not empty, remove the next node
# from the queue, swap its children, and add the children to the queue. Null nodes are not added to
# the queue. Eventually, the queue will be empty and all the children swapped, and we return the
# original root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def swap_node(self, root):
        if not root:
            return

        self.swap_node(root.left)
        self.swap_node(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp


    def invertTree(self, root: TreeNode) -> TreeNode:
        self.swap_node(root)
        return root


# We can acheive above logic in more concise way :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root 
