# Program for deleting key from binary search tree.
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


def findInorderSucessor(root):

    ptr = root
    while ptr.left:
        ptr = ptr.left

    return ptr

def deleteNode(root, key):

    if root == None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:

        if not root.left and not root.right:
            root = None
            return root

        elif not root.left and root.right:
            temp = root.right
            root = None
            return temp

        elif not root.right and root.left:
            temp = root.left
            root = None
            return temp

        else:
            temp = findInorderSucessor(root.right)
            root.data = temp.data
            root.right = deleteNode(root.right, temp.data)

    return root

from collections import deque
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


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root = deleteNode(root, 2)
    levelOrder(root)
