# Program for identifying the identical trees if it is, return True or False.
# --------------------------------------------------------------------------------
#Input : Roots of below trees
#    10           10
#  /   \         /
# 5     6       5
# As we can see in the above structure, in the second tree there is no right child,
# and hence return False.
# Input : Roots of below trees
#    10            10
#  /   \         /   \
# 5     6       5     6
# So, we can see here, both structures are very similar with same values and same arrangement
# of child nodes.
# So, there will no situation when there is some node in one of the tree and there is nothing
# in the other tree.
# So, return True.
# ---------------------------------------------------------------------------------
# Approach : It is clear that we need to traverse both the trees simulatenously,
# also , it will be top-down approach and preorder.
# So, we will see both approaches, preorder (recursive) as well as level order (iterative) using queues.
# So, if we do preorder, then base cases will be when we will be having empty trees, then we have to return True.
# Now, if there is this case where we got something on one of the trees and nothing on other tree, then we have to
# return False.

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def is_identical(root1, roo2):

    if root1 == None and root2 == None:
        return True

    if root1 and root2:
        return root1.data == root2.data and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

    return False

if __name__ == '__main__':
#
#         1                    1
#        / \                  / \
#       2   3                2   3
#      / \                  / \
#     4   5                4   5
    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    print(is_identical(root1, root2))
