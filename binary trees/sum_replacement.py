# Program for replacing every node by the sum of the all descendents.
# IDEA: so, we have to think that, we have replace the node not only by the just immediate descendents, but also by
# all the descendents possible from leaf to that node.
# So, we can apply and break down into some recurrence which suggests to compute sum of left part + sum of right part + current data
# This current data is important because once we replace the current node, we can't get that back, so we have to save it before replacing it.
# We can take example for follwoing tree and visualize stack call :
#            1   (6 + 8 + 1)
#          /  \
#(4+5+2) 2     3 (0 + 3)
#       /  \
# (0+0)4    5 (0+ 0)
# --------------------------------
# As we can see we need to go to every node and save the current data, and replace the node by sum of left subtree + sum of right subtree + current
# TIME : 0(N), SPACE: 0(N)

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque

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

def replace_node(root):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return root.data

    leftsum = replace_node(root.left)
    rightsum = replace_node(root.right)
    temp = root.data
    root.data = leftsum + rightsum
    return temp + root.data

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    levelOrder(root)
    replace_node(root)
    print()
    levelOrder(root)
