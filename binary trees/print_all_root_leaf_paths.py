# Program to print all the paths possible from root to leaves.
# ---------------------------------------------------------------------------
# IDEA: Logic is we can use recursion ,
# make a call to the traversePaths(root, path, pathLen)
# if base condition : root is None, return.
# if len(path) > pathLen : path[pathLen] = root.data, else path.append(root.data)
# pathLen += 1
# if leaf node is reached, if not root.left and not root.right: printArray(path, PathLen)
# else: printPathsRec(root.left, path, pathLen), printPathsRec(root.right, path, pathLen)
# ---------------------------------------------------------------------------
# But this would not be optimized as TIME : 0(N^2).
# ---------------------------------------------------------------------------
# SO, CAN WE DO BETTER ?
# what if we do some another traversal ? also we once we traverse to a path, we need a way
# to get back to root and traverse another path - that gives the idea we have already used
# in iterative preorder traversal using a extra stack.
# So, we can actually extend this preorder traversal (due to root -> leaf), and also
# maintain a hashmap containing keys as nodes and values as their parent.
# In this way, along with traversing the entire tree, when popping , we check if anytime
# we reached leaf node, then it means we have covered all elements in its path, then
# we can simply use the hashmap to link back up to the root and print the path.
# Similarly, we can do this for all other leaf nodes.
# ---------------------------------------------------------------------------
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# TIME : 0(N), AS ALL NODES ARE PROCESSED ATMOST ONCE

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printTopToBottom(curr, parent):

    stack = deque([])

    while curr:
        stack.append(curr)
        curr = parent[curr]

    while stack:
        temp = stack.pop()
        print(temp.data, end = "->")
    print()

from collections import deque

def printRootToLeaf(root):

    if root == None:
        return

    stack = deque([])
    stack.append(root)
    parent = {}
    parent[root] = None

    while stack:

        temp = stack.pop()

        if not temp.left and not temp.right:
            printTopToBottom(temp, parent)

        if temp.right:
            parent[temp.right] = temp
            stack.append(temp.right)

        if temp.left:
            parent[temp.left] = temp
            stack.append(temp.left)

# ------------------------------------------------------------------------------------------------
# IF WE NEED NOT PRINT AND STORE THE PATHS IN A LIST THEN SLIGHT MODIFICATIONS :
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def print_root_to_leaf(self, curr, parent):
#         res = ""
#         stack = deque()
#         while curr:
#             stack.append(curr)
#             curr = parent[curr]
#
#         while len(stack) > 1:
#             res = f"{res}{stack.pop().val}->"
#
#         if stack:
#             res = f"{res}{stack.pop().val}"
#
#         return res
#
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#
#         if root == None:
#             return
#
#         parent = {}
#         stack = deque()
#         stack.append(root)
#         parent[root] = None
#         result = []
#         while stack:
#
#             curr = stack.pop()
#             if not curr.left and not curr.right:
#                 result.append(self.print_root_to_leaf(curr, parent))
#
#             if curr.right:
#                 stack.append(curr.right)
#                 parent[curr.right] = curr
#
#             if curr.left:
#                 stack.append(curr.left)
#                 parent[curr.left] = curr
#         return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printRootToLeaf(root)
