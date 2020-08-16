# Program for flattening the binary tree into linked list.
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# It is to be converted to following
#
#     1
#      \
#        2
#         \
#          4
#           \
#            5
#             \
#              3
#
# Logic is simple to use any order, like preorder logic.
# So, we maintain a stack and push first the stack.
# Now, while stack not empty, pop off the stack (curr), then push first right, then push left and then, check if stack is not empty,
# then, curr.right = stack[-1]
# and also make curr.left = None.
# -----------------------------------------------------------------------------------

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque
def flatten(root):
    if root == None:
        return

    stack = deque()
    stack.append(root)
    while stack:
        
        curr = stack.pop()
        if not curr.right:
            stack.append(curr.right)
        if not curr.left:
            stack.append(curr.left)

        if stack:
            curr.right = stack[-1]

        curr.left = None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    flatten(root)
    print(root.right.data)
