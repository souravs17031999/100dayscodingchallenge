# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# HINTS :
# First thing is to note that we need a ascending order sored type iterator
# leftmost element is the smallest of the tree.
# ---------------------------------------------------------------------------------------------------
# We can use a stack and push all the left most elements one by one from root to leaf onto stack in the initialiation part.
# Now, we can pop off the stack while calling the next(), after which also we need to point to right and then again push all the
# left elements onto the stack starting from this right (popped element right).
# ----------------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = deque()
        ptr = root
        while ptr:
            self.stack.append(ptr)
            ptr = ptr.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ptr = self.stack[-1].right
        temp = self.stack.pop().val
        while ptr:
            self.stack.append(ptr)
            ptr = ptr.left
        return temp

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
