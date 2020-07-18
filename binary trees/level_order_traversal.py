# Program to print level order traversal for the binary tree
# APPROACH : Approach is to think that for level order, we first expand
# whatever is explored first, in breadth wise manner, that is we need to
# have some buffer which can store next set of elements to be explored once we
# finish exploring current element.
# That is we need some intermediate structure, here "queue" which uses this
# property of first in first out.

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

    while queue:

        temp = queue.popleft()
        print(temp.data, end = " ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

# driver test function
if __name__ == '__main__':
    root = Node(13)
    root.left = Node(12)
    root.right = Node(10)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right.left = Node(16)
    root.right.right = Node(9)
    levelOrder(root)
