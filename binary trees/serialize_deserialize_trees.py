# Program for serialization and deserialization of binary trees.
# -------------------------------------------------------------------------------------
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or
# memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#            1
#           / \
#          2   3
#             / \
#            4   5
# -------------------------------------------------------------------------------------------
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
# Input: root = [1,2]
# Output: [1,2]
# --------------------------------------------------------------------------------------
# LOGIC FOR serialization :
# Now, important key is to think in terms of traversals -
# Preorder is kind of good to go !
# We can simply store preorder traversal and store a bit with every node to indicate
# whether the node is an internal node or a leaf node.
# A NULL Marker "," or "X" can be used to mark None nodes.
# ------------------------------------------------------------------------------------------
# LOGIC FOR deserialization :
# We can keep and maintain a Queue, which can track the progress in every recursive call and create
# a new node for every valid node value otherwise ignore None.
# ------------------------------------------------------------------------------------------
#
#            1
#           / \
#          2   3
#             / \
#            4   5
# -------------------------------------------------------------------------------------------
from collections import deque

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def serialize_helper(root, A):
    if root == None:
        return "X"

    lstring = serialize_helper(root.left, A)
    rstring = serialize_helper(root.right, A)
    temp = "".join((str(root.data) + ' ' + lstring + ' ' + rstring))
    A.append(temp)
    return temp

def serialize(root, A):
    serialize_helper(root, A)
    return A[-1].split(" ")

def deserialize_helper(queue):

    if queue:
        curr = queue.pop()
    if curr == 'X':
        return None

    new_node = Node(curr)
    new_node.left = deserialize_helper(queue)
    new_node.right = deserialize_helper(queue)
    return new_node


def deserialize(A):
    queue = deque()
    for i in A:
        queue.append(i)
    return deserialize_helper(queue)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    r = serialize(root, [])
    print(r)
    print(deserialize(r))
