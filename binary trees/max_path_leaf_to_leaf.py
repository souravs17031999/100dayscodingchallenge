# program for computing the maximum sum for path from a leaf node to any leaf node.
# The logic is to think about cases, and combine the result and update the result for max
# in every recursion call , for root.left, and then root.right.
# ---------------------------------------------------------------------------------------
#
#
#                                   -15
#                                 /    \
#                                5      6*
#                              / \     / \
#                             -8  1   3*   9*
#                            / \           \
#                           2   6           0*
#                                          / \
#                                         4   -1*
#                                             /
#                                            10*
#
# here, max sum : 3 + 6 + 9 + 0 + -1 + 10 => 27   [* shows path in binary tree above]
# ---------------------------------------------------------------------------------------------
# TIME : 0(N), AS ALL THE NODES ARE PROCESSED ONLY ONCE .

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def compute_max_path(root, res):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return root.data

    lsum = compute_max_path(root.left, res)
    rsum = compute_max_path(root.right, res)

    if root.left and root.right:
        res[0] = max(res[0], lsum + rsum + root.data)
        return max(lsum, rsum) + root.data

    if root.left == None:
        return rsum + root.data
    if root.right == None:
        return lsum + root.data

import sys
if __name__ == '__main__':
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.left.left = Node(2)
    root.left.right = Node(1)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)
    res = [-sys.maxsize-1]
    compute_max_path(root, res)
    print(res[0])
