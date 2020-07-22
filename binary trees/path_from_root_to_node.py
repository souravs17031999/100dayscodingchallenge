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


# At every node, we check if it's the root data , if not
# then, we check for left subtree and right subtree.
def findPath(root, path, k):

    if root == None:
        return False


    path.append(root.data)
    if root.data == k:
        return True

    if root.left and findPath(root.left, path, k) or root.right and findPath(root.right, path, k):
        return True, path

    path.pop()
    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(findPath(root, [], 5))
