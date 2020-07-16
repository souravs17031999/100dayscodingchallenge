# Program to insert any given value in the binary tree.
# # IDEA: Since binary tree doesnt have any constraints, then we find first position avaiable from left most side
# and keep checking only we have a empty either left child or right child.
# Then, we simply create that node and append it to that position of new parent.
# Also, we should understand that how are we actually going to traverse the tree for finding the position ?
# Now, since we are going to write iterative solution, then we should understand we need to go level by level
# to find the first avaiable position in the manner described above.
# For level order traversal, we can also apply queue to make temporary buffer for storing children of cur node.
# Why queue ? because we check first parent , then children, then first left children, then rigt children
# this order can be maintained by using the queue.
# TIME : 0(N), SPACE : 0(N), N IS NUMBER OF NODES IN THE TREE.

from collections import deque

# Tree node structure class
class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# binary tree structure class
class binaryTree:

    # function for inserting into the tree by finding first avaiable position
    def insert(self, root, key):

        # base case, for empty tree
        if root is None:
            root = Node(key)
            return root

        queue = deque([]) # initialise queue using deque due to high performace
        queue.append(root) # append first element (given root as input), also we are appending complete node to it, not only value.


        # iterate till queue is empty
        while queue:

            # took off top of element
            temp = queue.popleft()

            # if left is not there, then we found a position
            if not temp.left:
                new_node = Node(key)
                temp.left = new_node
                break

            # otherwise simply append that child to queue
            else:
                queue.append(temp.left)

            # if right is not there, then we found a position
            if not temp.right:
                new_node = Node(key)
                temp.right = new_node
                break

            # otherwise simply append that child to queue
            else:
                queue.append(temp.right)

        return root

    # doing level order traversal (BFS) for printing the tree nodes (elements)
    def pretty_print(self, root):

        if not root:
            return

        queue = deque([])
        queue.append(root)

        while queue:

            temp = queue.popleft()
            print(temp.data, end = " ")
            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)
        print()


# driver test function
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    b = binaryTree()
    b.pretty_print(root)
    b.insert(root, 12)
    b.pretty_print(root)
