# Program to count and get sum of left leaf nodes in the binary tree.
# ------------------------------
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# We can use any iterative traversal for traversing every node, and check if current.left.left is None and current.left.right is None, then
# we include its sum in the overall sum, and we do this for every current.left node.
# --------------------------------
# We can also use recursive approach to solve this , we go for every node, if the root is not None, then check if root.left is leaf node or not ,
# if it's leaf node, then we simply add the root.left.data to the res.
# Now, if it's the not the leaf node, then we recur for left sub tree.
# and we every recur for right sub tree.
# So, all in all, we recur for both left and right subtrees, but while we go for left, we need to check specifically for leav nodes. That's it.
# NOTE : HEre, simply recurrence relation like adding left leav(leftsubtree) + right leav(rightsubtree) will not work.
# -----------------------------------
# TIME : 0(N), SPACE : 0(N).

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# function to check if it is leaf node
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

# recursive function to find the sum of all left leaf nodes
def sum_leaf(root):

    res = 0
    if root:

        if isLeaf(root.left):
            res += root.left.data
        else:
            res += sum_leaf(root.left)

        res += sum_leaf(root.right)

    return res

# driver function
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(9)
    root.right = Node(49)
    root.right.left = Node(23)
    root.right.right = Node(52)
    root.right.right.left = Node(50)
    root.left.left = Node(5)
    root.left.right = Node(12)
    root.left.right.right = Node(12)
    print(sum_leaf(root))
