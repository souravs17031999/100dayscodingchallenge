# Program for connecting all the nodes at the same level of binary tree
# NOTE: You'll be given an addition nextRight pointer for the same.
# --------------------------------------------------------------------------
#
#         10                      10 -> None
#        /  \                    /  \
#      3     5      =>         3---->5 -> None
#     / \     \               / \     \
#    4   1     2             4->1 ---->2 -> None
#
# Initially, all the nextRight pointers point to garbage values.
# Your function should set these pointers to point next right for each node.
# ---------------------------------------------------------------------------
# Naive solution is to level order BFS  and keep a track of all nodes at same level and then connect them one by one
# BUt this will take 0(N^2) as shown below :
from collections import deque
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.nextRight = None

def fix_right_pointer(root):

    if root == None:
        return

    queue = deque()
    queue.append(root)
    while queue:

        n = len(queue)
        temp = []
        for i in range(n):
            curr = queue.popleft()
            temp.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        for i in range(n - 1):
            temp[i].nextRight = temp[i + 1]

# -----------------------------------------------------------------------------------------------
# OPTIMIZED IN 0(N) : USING NULL DELIMITER LOGIC, WE CAN MARK NEXT LEVEL, AND THEN every time we pop element from queue
# already the element at front  of queue is the one which is to be set to the nextRight pointer of popped element.
# This will take only 0(N) as only atmost one node is processed.

def connect_right_pointer(root):

    queue = deque()
    queue.append(root)
    queue.append(None)

    while queue:
        curr = queue.popleft()
        if curr == None:
            if queue:
                queue.append(None)
        else:
            curr.nextRight = queue[0]
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(3)
    root.right = Node(5)
    root.right.right = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(1)
    connect_right_pointer(root)
    print(root.left.nextRight.data)
    print(root.left.left.nextRight.data)
    print(root.left.right.nextRight.data)
