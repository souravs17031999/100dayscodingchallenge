# Program for Checking if the given binary tree is binary search tree or not.
# APPROACH :
# one of the key observations is that, if we just check that for the root node
# if left subtree is BST and if the right subtree is BST, then overall BST isn't
# necessarily the BST and this can be seen in the following :
# ACTUALLY, this condition is compulsory but not sufficient.
# -----------------------------------------------
#                     5
#                   /   \
#                 3      20
#               /  \    /  \
#             1    10   12  50
#
# As we can see here, for every node, BST property follows but then also, at
# it is not BST as "10" should not be on the left side of root = 5.
# -----------------------------------------------
# So, if we think carefully, then we can observe that root should lie between a
# defined range,  max (left subtree) < root < min (right subtree)
# As if root is greater than min of left subtree, then it is greater than all other values which are lesser than this value.
# and similarly, if this is lesser than greater max value from right subtree, then
# it is obviosuly, lesser than all other greater values.
# -----------------------------------------------------
# So,we can combine both of the above conditions into the existing necessary conditons
# Also, we can follow Both top down and bottom up approach ,
# In bottom up approach, we will create pair/triple reutnrin a tuple() for evevry node
# containing(min, max, bool)bool denotes if it's left and rihgt subtree is BST or not.
# Whereas in top down approach, we can simply follow preorder type traversal.
# --------------------------------------------------------
# TOP DOWN APPROACH :

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None



def isBST(root, minV, maxV):

    if root == None:
        return True

    if root.data >= minV and root.data <= maxV and isBST(root.left, minV, root.data) and isBST(root.right, root.data, maxV):
        return True

    return False


import sys
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    MIN_VAL, MAX_VAL = - sys.maxsize - 1, sys.maxsize
    print(isBST(root, MIN_VAL, MAX_VAL))
