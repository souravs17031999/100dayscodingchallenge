# Program for computing height of the binary tree.
# Height is simply the longest path from root to the leaf node.
# IDEA: Approach is to as always break down the into recursive approach, and observing that height of the tree
# is maximum of the (height of left subtree, height of right subtree) + 1.
# So, in this way, as every node we compute max(left subtree, right subtree)  + 1.
# We can take example for follwoing tree and visualize stack call :
#       (3)  1
#          /  \
#   (2)  2     3  (1)
#       /  \
#  (1) 4    5 (1)
# --------------------------------

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# recursive function to compute the height of the tree
# height(root) = 1 + max(height(root.left), height(root.right))
def height(root):

    if root == None:
        return 0

    return 1 + max(height(root.left), height(root.right))

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(height(root))
