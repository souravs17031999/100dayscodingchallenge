# Program for binary search tree Introduction
# Binary search Tree has following property :
# Every root has left child smaller ,
# Every root has right child greater.
# Every node will also satisfy that its left and right subtree will also be BST.
# So, each left subtree will contain values less than the root, and each right subtree
# will contain values greater than the root.

# ------------------------------------------------------------------
# Inorder traversal of BST always produces sorted output.
# We can construct a BST with only Preorder or Postorder or Level Order traversal.
# Note that we can always get inorder traversal by sorting the only given traversal.
# Number of unique BSTs with n distinct keys is Catalan Number
# ------------------------------------------------------------------

# Therefore, insertion, deletion and searching takes 0(lg(N)) on average but in worst case
# it will be 0(N) time.
# WE CAN TAKE FOLLOWING EXAMPLE FOR VISUALIZING :
# --------------------------------------------# ----------------------------------------------------
#            4
#          /  \
#        2     5
#       /  \
#      1    3
# --------------------------------
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
