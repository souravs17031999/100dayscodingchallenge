# Program for binary trees introduction
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(root.data)
    print(root.left.data)
    print(root.right.data)
    print(root.left.left.data)

#       1
#      / \
#      2  3
#     /
#   4
