# Program to print the right view , for the binary tree.
# ----------------------------------------------------------
# EXAMPLE  :
#                         8
#                       /   \
#                     10     3
#                    /  \     \
#                    1   6      14
#                        /\      /
#                       9  7   13
#
# This would give me : 8, 3, 14, 13
# -----------------------------------------------------------------
# APPROACH : One simple approach is to use level order traversal, and we can see this is a problem of top-down
# traversal.
# Now, at any point the queue, it contains the children of that level, while queue is not empty, we can
# traverse each node at each level and print the last node at that level.
# TIME : 0(N), SPACE : 0(W), W IS WIDTH OF BINARY TREE., WORST CASE : BOTTOM OF TREE HAS MAX NUMBER
# OF NODES WHICH IS 2^(H - 1).
# CAN WE DO BETTER THAN THIS ?
# ---------------------------------------------------------------------
# So, as we observed that it is a top down traversal problem, and so we can think of preorder type traversal.
# Now, preorder goes like left first, then right, but here we have to go for right first, and then left
# due to right view , and also we need to have some parameter for recursive call which will define if there is a
# change in the level or not.
#
# ---------------------------------------------------------------------

# Used the second approach
from collections import deque

class Node:
    """Node structure """
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# ---------------------------------------------------------
# FIRST APPROACH :
# function for level order traversal for binary tree
def levelOrder(root):

    if not root:
        return

    queue = deque([])
    queue.append(root)
    while queue:

        n = len(queue)

        for i in range(1, n + 1):

            temp = queue.popleft()

            if i == n:
                print(temp.data, end = " ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


# SECOND APPROACH :
# -------------------------------
# So, here maxlevel should be passed as reference , as we do not need to change this value in every
# recursive call, and hence, we pass this as a list element which basically passes by reference.
# ---------------------------------
def printRightView(root, level, maxlevel):
    if root == None:
        return

    if maxlevel[0] < level:
        print(root.data, end = " ")
        maxlevel[0] = level

    printRightView(root.right, level + 1, maxlevel)
    printRightView(root.left, level + 1, maxlevel)

# driver test function
if __name__ == '__main__':
    root = Node(8)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(9)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    maxlevel = [-1]
    printRightView(root, 0, maxlevel)
