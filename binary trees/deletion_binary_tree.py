# Program for deletion of node in the binary tree.
# APPROACH : Since, we can see here there is no order unlike BST's, so we will simply
# delete the node by searching it and also swap the node with the last element and so
# the tree decreases in height from bottom.
# TIME : 0(N), SPACE : 0(N).

from collections import deque

class Node:
    """Node structure """
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# function for deleting the rightmost node (deepest node)
# Searching level order for right most and set it to None
def delete_deepest(root, d_node):

    # initialising queue
    queue = deque([])
    queue.append(root)

    # iterate till queue is empty
    while queue:

        temp = queue.popleft()
        if temp == d_node:
            temp = None
            return

        # if left child exists, and equal to given d_node, then
        # set the next (that is left) is None
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return

            else:
                queue.append(temp.left)

        # if right child exists, and equal to given d_node, then
        # set the next (that is right) is None
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)


# function to delete the node given as input
def delete_node(root, node):

    if not root:
        return

    queue = deque([])
    queue.append(root)

    # we initialise key_node to None and search for the given node
    # as input
    key_node = None

    while queue:

        temp = queue.popleft()

        # when we find the node, then we set key_node to the searched
        # data
        if node == temp.data:
            key_node = temp

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    # if we found our given node (given as input) to be deleted
    # then swap the data and delete it.
    if key_node:
        x = temp.data
        delete_deepest(root, temp)
        key_node.data = x

    return root

# function for printing the tree using levelOrder, we can also
# inorder, postorder, preorder traversal.
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

    print()

# driver test function
if __name__ == '__main__':
    root = Node(13)
    root.left = Node(12)
    root.right = Node(10)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right.left = Node(16)
    root.right.right = Node(9)
    levelOrder(root)
    root = delete_node(root, 12)
    levelOrder(root)
    root = delete_node(root, 13)
    levelOrder(root)
    root = delete_node(root, 13)
    levelOrder(root)
    root = delete_node(root, 10)
    levelOrder(root)
    root = delete_node(root, 4)
    levelOrder(root)
    root = delete_node(root, 16)
    levelOrder(root)
