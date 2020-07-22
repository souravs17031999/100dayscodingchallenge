# Program to print level by level order traversal each levels on a new line , for the binary tree.
# -----------------------------------------------------------------
# APPROACH : One way to approach is to store a pair of (node, level) info in BFS queue,
# and when we insert new children, we increase their level by 1 (by seeing their parent level), similarly
# when we pop, again we check if their is any transition from last popped with current popped item
# in terms of level, then we know this is the new level.
# ----------------------------------------------------------------
# Now, Second approach would be to use a "None" value, whenever we encounter a already None value while
# popping out, also on the start we push root and None both so that next time we would enounter None and know that
# we have crossed first level, similarly, whenerv we encounter None while popping out, we push another None,
# while the stack is not empty, if at any time stack is empty after popping, we stop.
# ----------------------------------------------------------
# EXAMPLE  :
#                         8           8
#                       /   \
#                     10     3        10, 3
#                    /  \     \
#                    1   6      14    1, 6, 14
#                        /\      /
#                       9  7   13     9, 7, 13
# ----------------------------------------------------------------
# TIME : 0(N), SPACE : 0(W), W IS WIDTH OF BINARY TREE.

# Used the second approach
from collections import deque

class Node:
    """Node structure """
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# function for level order traversal for binary tree
def levelOrder(root):

    if not root:
        return

    queue = deque([])
    queue.append(root)
    queue.append(None)
    while queue:
        temp = queue.popleft()
        if temp == None:
            print()
            if queue:
                queue.append(None)

        else:

            print(temp.data, end = " ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

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


    levelOrder(root)
