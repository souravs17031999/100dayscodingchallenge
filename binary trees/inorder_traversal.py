# Program for inorder traversal for a binary tree
# --------------------------------
# As we know inorder traversal means, Left-Node-Right
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
#
# RECURSIVE APPROACH
# --------------------------------
# TIME : 0(N), SPACE : NOT CONSTANT, DUE TO RECURSIVE CALLS.
# WE should also try to write iterative solution, because there might
# be some case where stack recursion depth limit is exceeded due to not
# enough memory available or due to system limit on recursion calls.
# ---------------------------------------
# ITERATIVE SOLTUION :
#Push the current node to S and set current = current->left until current is NULL
# If current is NULL and stack is not empty then
#    * Pop the top item from stack.
#    * Print the popped item, set current = popped_item->right
#    * Go to step 3.
# If current is NULL and stack is empty then we are done.
# ---------------------------------------------
# TIME : 0(N), SPACE : 0(N) WHERE N IS THE NUMBER OF NODES IN THE TREE.
# ----------------------------------------------
# we can also optimized more on space complexity part by not using any
# stack or recursion, named as "MORRIS TRAVERSAL" which is described in
# MORRIS_traversal.py in a separate program.
# ----------------------------------------------

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# inorder recursive
def inorder_rec(root):

    if root == None:
        return

    inorder_rec(root.left)
    print(root.data, end = " ")
    inorder_rec(root.right)


# ITERATIVE SOLUTION :
from collections import deque

def inorder_itr(root):

    if root == None:
        return

    stack = deque([])
    ptr = root
    while True:
        # this will be true everytimee until ptr.left becomes None,
        # that means all the left ones will be on the stack firstly.
        if ptr:
            stack.append(ptr)
            ptr = ptr.left

        # now when above fails, then we need to pop the top of stack
        # and print it, also make current ptr to ptr.right to traverse
        # for right subtree
        elif stack:
            ptr = stack.pop()
            print(ptr.data, end = " ")

            ptr = ptr.right

        # now if current ptr is also None and stack is also empty,
        # then we need to move out of loop.
        else:
            break


# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #inorder_rec(root)
    inorder_itr(root)
