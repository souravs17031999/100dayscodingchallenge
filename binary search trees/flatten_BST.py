# Program to flatten BST into sorted linked list
# APPROACH :
# Now, inorder traversal will be the correct output but this is a sort of Hack.
# We can actually use bottom up approach and use Pair - tuple (head, tail)
# and every node returns this tuple.
# Now, there can four cases,
# First : if there is only left subtree for the root,
# then, we simply need to point tail for last node to root.
# Second : if there is only right subtree for the root,
# we simply add the root to the head and now its the new head.
# Third : Now, if there is only one node, return this root node.
# Fourth : If both left and right subtree exists, then we need to point tail of first linked list
# to the root node, and add the root node to the head of second linked list.


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

def flatten(root):
    l = LinkedList()

    # base case
    if root == None:
        l.head = l.tail = None
        return l

    # only root node exist
    if not root.left and not root.right:
        l.head = l.tail = None
        return l

    # if only left subtree exists
    if root.left and not root.right:
        leftLL = flatten(root.left)
        leftLL.tail.right = root

        l.head = leftLL.head
        l.tail = root
        return l

    # if only right subtree exists
    if root.right and not root.left:
        rightLL = flatten(root.right)
        root.right = rightLL.head

        l.head = root
        l.tail = rightLL.tail
        return l

    # if both subtree exists
    leftLL = flatten(root.left)
    rightLL = flatten(root.right)

    l.head = leftLL.head
    l.tail = rightLL.tail

    return l

# driver testing function
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(flatten(root).head)
    print(flatten(root).tail)
