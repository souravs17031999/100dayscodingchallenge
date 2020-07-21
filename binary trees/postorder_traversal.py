# Program for postorder traversal for a binary tree
# --------------------------------
# As we know postorder traversal means, left-Right-Node
# --------------------------------
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# RECURSIVE APPROACH
# --------------------------------
# TIME : 0(N), SPACE : NOT CONSTANT, DUE TO RECURSIVE CALLS, 0(N).
# ---------------------------------------------------
# ITERATIVE APPROACH :
# Now, we can apply the same approach as preorder logic, but now we need to push left subtree first,
# and push right subtree then since we know stack follows LIFO ordering, and also if we simply print the node by popping and then inserting
# left and then right, then we will get reversed postorder and so we need one more stack to reverse this ordering to get
# original postorder ordering.
# ---------------------------------------------------
# TIME : 0(N), SPACE : 0(N).
# --------------------------------------
# Can we do better ? , more space can be optimized by using only one stack :
# Do following while root is not NULL
#    * Push root's right child and then root to stack.
#    * Set root as root's left child.
# Pop an item from stack and set it as root.
#    * If the popped item has a right child and the right child
#       is at top of stack, then remove the right child from stack,
#       push the root back and set root as root's right child.
#    * Else print root's data and set root as NULL.
# Repeat steps 2.1 and 2.2 while stack is not empty.
# --------------------------------------
# TIME : O(N), SPACE: (N) [BUT LESS THAN ORIGINAL ONE IF WE CONSIDER IN TERMS OF PRACTICALITY]

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# recursive approach
def postorder_rec(root):

    if root == None:
        return

    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.data, end = " ")

# iterative approach
from collections import deque

def postorder_itr(root):

    if root == None:
        return

    stack1, stack2 = deque([]), deque([])

    # first, push root, then while stack1 is not empty, pop from stack1 and push to stack2,
    # then, push left child and then push right child onto stack1.
    stack1.append(root)
    while stack1:

        temp = stack1.pop()
        stack2.append(temp)
        if temp.left:
            stack1.append(temp.left)

        if temp.right:
            stack1.append(temp.right)

    # now, we have got reversed postorder ordering on stack2
    # keep popping and printing which will give original postorder ordering.
    while stack2:

        temp = stack2.pop()
        print(temp.data, end = " ")

# --------------------------------------
# MORE SPACE OPTIMIZED APPROACH :
# --------------------------------------
# function to look and retunr the top of stack if it exists
def peek(stack):
    if len(stack):
        return stack[-1]

    return None

# FUNCTION TO traverse according to above said space optimized approach     
def postorder_itr_mod(root):

    if root == None:
        return

    stack = deque([])

    while True:

        while root:

            if root.right:
                stack.append(root.right)
            stack.append(root)

            root = root.left

        root = stack.pop()

        if root.right and root.right == peek(stack):
            stack.pop()
            stack.append(root)
            root = root.right

        else:
            print(root.data, end = " ")
            root = None

        if len(stack) <= 0:
            break


# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #postorder_rec(root)
    postorder_itr(root)
    print()
    postorder_itr_mod(root)
