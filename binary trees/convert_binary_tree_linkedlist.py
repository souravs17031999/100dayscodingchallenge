# Program for converting binary tree into flattened linked list
# -----------------------------------------------------------------------------
# One of the key things is to visualize following diagram in mind :
#
#               1                    1              1
#              /\                   / \              \
#             2  5            =>   2   5     =>        2
#            /\   \                 \   \               \
#           3 4    6                 3   6                3
#                                     \                    \
#                                      4                     4
#                                                              \
#                                                               5
#                                                                \
#                                                                 6
# ----------------------------------------------------------------------------
# If we think about the above process, it will be easily done with firstly checking if left leaf is not None,
# then we need to move left part of the tree to its right part for that particular root node.
# this should be done recursively for every node in the tree and it will be flattened.
# ----------------------------------------------------------------------------
# TIME : 0(N)

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# RECURSIVE SOLUTION : USING THE ABOVE LOGIC ---------------------------------
def flatten(root):

    # if root is NUll or if leaf node then return
    if root == None or (root.left == None and root.right == None):
        return

    # if root.left exists, then we have to make it root.right
    if root.left != None:

        # move left recursive
        flatten(root.left)

        # store the root.right node
        temp = root.right
        # fix the right so that left subtree rooted at root comes at right of it
        root.right = root.left
        # nullify the left part
        root.left = None

        # now we store the newly fixed right node
        ptr = root.right
        # find the position where we need to attach the previously stored temp (older right node )
        while ptr.right:
            ptr = ptr.right

        # attach the older right to the right of new right (making it flattened)
        ptr.right = temp

    # recurisvely call for right subtree
    flatten(root.right)

# -----------------------------------------------------------------------------
# ITERATIVE SIMPLE LOGIC : USING STACK AND SAME ABOVE LOGIC
# IF WE OBSERVE CAREFULLY, and only focus on one root node,
#
#            1           1
#          / \      =>    \
#         2   3            2
#                           \
#                            3
# -----------------------------------------------------------------------------
# We can think that if we store the address of right node, then shift left node to the root.right, then again
# fix that stored node as right of current newly made right node, it will be flattened.
# If there will be more nodes (more than one on right), then we can maintain a stack for all those nodes .
# ------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(log(N))

from collections import deque

def flatten_list(root):

    stack = deque()
    ptr = root
    while root or stack:

        if root.right:
            stack.append(root.right)

        root.right = root.left
        root.left = None

        if root.right == None and stack:
            root.right = stack.pop()

        root = root.right

    return ptr

# helper function to print inorder traversal
def inorder(root):

    if root == None:
        return

    inorder(root.left)
    print(root.data, end= " ")
    inorder(root.right)

# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    inorder(root)
    flatten_list(root)
    print()
    inorder(root)
