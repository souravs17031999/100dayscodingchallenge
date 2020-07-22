# Program for inserting key into binary search tree.
# WE CAN TAKE FOLLOWING EXAMPLE FOR VISUALIZING :
# ----------------------------------------------------
#            4
#          /  \
#        2     5
#       /  \
#      1    3
# --------------------------------
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

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

def insert(root, key):

    if root == None:
        root = Node(key)
        return root

    if key <= root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root

def insert_itr(root, key):
    ptr = root
    while ptr:

        if ptr.data <= key:
            ptr = ptr.right
        else:
            ptr = ptr.left

    ptr = Node(key)

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root = insert(root, 7)
    levelOrder(root)
