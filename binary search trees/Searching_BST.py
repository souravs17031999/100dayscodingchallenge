# Program for searching for key into binary search tree.
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


def search(root, key):


    if root == None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(search(root, 39))
