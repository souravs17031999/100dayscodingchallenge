# Program to compute maximum path sum through any two node in the binary tree.
# Approach :
# IDEA: First, we have to think about three possibilities that may occur in a binary tree, like max sum
# may go through root, or may not go through root, now if not going through root, then it may be there,
# that max sum is formed using only left subtree or it may be there max sum may be formed using right subtree
# Now, it maybe possible that the sum we choose for going through the root maybe max of following four options:
# * root
# * root + root.left
# * root + root.right
# * root + left + right
# The above four cases result from the observation that the binary tree consists of negative numbers also,
# so, let' say that left subtree contains negative numbers and so we basically will not consider left branch
# anymore, and choose from remaining any three of them, similarly for other three options for this category.
# Now, this is for first case when we consider going through root, now similary we can consider for left subtree and right subtree and get the overall max from the main three options we discovered.
# NOTE : since we have to find maximum distance between any two give node, then we follow
# bottom up approach postorder type approach.
# We recur for left first, then recur right and now node pair is processed and we update
# pair tuple with (branchsum, maxsum).
# -------------------------------
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Pair:

    def __init__(self):
        self.branchsum = 0
        self.maxsum = 0


def maxSumPath(root):

    p = Pair()

    if root == None:
        return p

    left = maxSumPath(root.left)
    right = maxSumPath(root.right)

    op1, op2, op3, op4 = root.data, left.branchsum + root.data, right.branchsum + root.data, root.data + left.branchsum + right.branchsum

    current_ans_through_root = max(op1, max(op2, max(op3, op4)))

    p.branchsum = max(left.branchsum, max(right.branchsum, 0)) + root.data
    p.maxsum = max(left.maxsum, max(right.maxsum, current_ans_through_root))

    return p

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(maxSumPath(root).maxsum)
