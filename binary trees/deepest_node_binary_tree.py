# Program for finding the deepest node in the tree.
# Input : Root of below tree
#             1
#           /   \
#          2      3
#         / \    / \
#        4   5  6   7
#                    \
#                     8
# Output : 8
#
# Input : Root of below tree
#             1
#           /   \
#          2      3
#                /
#               6
# Output : 6

# ----------------------------------------------------------------------------------------------------
# As we know that height of the binary tree is the maximum depth of the binary tree.
# From calculating height, we know that max. depth which is the level of the deepest node
# and then we can print the node data at the level as found above.

# TIME : 0(N), N IS NODES OF BINARY TREE.

class new_Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def height(root):

    if not root:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) + 1

def deepest_node(root, levels):

    if not root:
        return

    if levels == 1:
        print(root.data)

    elif levels > 1:
        deepest_node(root.left, levels - 1)
        deepest_node(root.right, levels - 1)

if __name__ == '__main__':

    root = new_Node(1)
    root.left = new_Node(2)
    root.right = new_Node(3)
    root.left.left = new_Node(4)
    root.right.left = new_Node(5)
    root.right.right = new_Node(6)
    root.right.left.right = new_Node(7)
    root.right.right.right = new_Node(8)
    root.right.left.right.left = new_Node(9)

    levels = height(root)

    deepest_node(root, levels)
