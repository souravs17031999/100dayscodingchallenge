# Program for conversion of binary tree to doubly linked list.
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# For the above inorder traversal : 4 2 1 5 3
# In the same way, we will create doubly linked list in inorder traversal.

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def convert_double(root, head, prev):

    if root == None:
        return

    convert_double(root.left, head, prev)
    if prev[0] == None:
        head = root
        print(head.data)
    else:
        root.left = prev[0]
        prev[0].right = root

    prev[0] = root
    convert_double(root.right, head, prev)

def print_list(head):

    ptr = head
    print("HEY")
    while ptr:
        print(ptr.data, end = " ")
        ptr = ptr.right

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    head = None
    prev = [None]
    convert_double(root, head, prev)
