# Program for checking whether given tree is symmetric tree
# ---------------------------------------------------------------------------
#
#                1
#              /  \
#             2    2               => True
#           /  \   / \
#          3    4 4   3
#
#
#            1
#           / \
#          2   2               => False
#          \    \
#           3    3
#
# ----------------------------------------------------------------------------
# We can observe following facts, for the symmetrical tree :
# firstly, root data must be same, then root.left == root.right,
# root.left.left == root.right.right, then root.left.right == root.right.left
# ----------------------------------------------------------------------------
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def is_symmetric(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 and root2:
        return root1.data == root2.data and is_symmetric(root1.left, root2.right) and is_symmetric(root1.right, root2.left)

    return False

def check_symmetric(root):
    return is_symmetric(root, root)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(check_symmetric(root))
