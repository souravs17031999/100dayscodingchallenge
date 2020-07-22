# Program to count and get sum of leaf nodes in the binary tree.
# ------------------------------
# We can take example for follwoing tree and visualize stack call :
#        (2, 1)  1
#              /  \
#    (1, 1)  2     3 (0, 0)
#          /  \
#  (0, 0) 4    5  (0, 0)
# --------------------------------
# We can actuall the following recurrence relation as we observe
# count_leaf(root) = count_leaf(root.left) + count_leaf(root.right)
# -----------------------------------------
# BASE CASES :
# so, if root == None, return 0
# so, if root.left, root.right is None, return 1
# -----------------------------------------

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def count_leaf(root):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1

    return count_leaf(root.left) + count_leaf(root.right)

def sum_leaf(root):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return root.data

    return sum_leaf(root.left) + sum_leaf(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(count_leaf(root))
    print(sum_leaf(root))
