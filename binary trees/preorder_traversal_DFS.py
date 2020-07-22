# Program for preorder traversal for a binary tree
# --------------------------------
# As we know preorder traversal means, Node-Left-Right, so we can recursively
# at every node, call preorder func and print the data at current node,
# and goto left and then goto right (for every node).
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
#
#  stack : print "1", 1(L), print "2", 2(L), print "4", 4(L) -> 4L is None - >  return, base case -> 4R is None -> return, base case
#          print "1", 1(L), print "2", 2(L)
#          print "1", 1(L), print "2", 2R -> print "5", 5(L) is None - >  return, base case -> 5(R) is None -> return, basecase
#          print "1", 1(L),
#          print "1", 1(R)
#          print "1", print "3", 3(L) is None - >  return, base case -> 3(R) is None -> return, basecase
#          stack empty
# --------------------------------
# TIME : 0(N), SPACE : NOT CONSTANT, DUE TO RECURSIVE CALLS.
#-----------------------------
# ITERATIVE APPROACH
# We can also use iterative approach, where we use explicit stack and push the root first.
# Now, we pop off the top of stack, then push right child first, then push left child first
# This, is done to process left subtree first, so that popping will print left child first.
#-----------------------------
# TIME : 0(N), SPACE : 0(N).
# --------------------------------------
# We can again improve on space complexity part, by only storing right child elements onto stack , this is because preorder considers processing all left ones first and then it goes
# for right ones, so we can then keep on printing the stack top one by one.
# --------------------------------------
# TIME : 0(N), SPACE : 0(H), H IS HEIGHT OF TREE.

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# recursive approach
def preorder_rec(root):

    if root == None:
        return

    print(root.data, end = " ")
    preorder_rec(root.left)
    preorder_rec(root.right)

# iterative approach
from collections import deque

def preorder_itr(root):

    if root == None:
        return

    stack = deque([])
    stack.append(root)
    while stack:

        temp = stack.pop()
        print(temp.data, end = " ")

        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)

    print()

# MORE SPACE OPTIMIZED APPROACH :
def preorder_itr_mod(root):

    if root == None:
        return

    # FIRSTLY WE iterate and keep printing left one's and push right child onto stack
    # (if it exists)
    stack = deque([])
    ptr = root

    while ptr:
        print(ptr.data, end = " ")

        if ptr.right:
            stack.append(ptr.right)
        ptr = ptr.left

    # Now, we check if we have reached the end of left ones, then we start printing
    # right ones using stack until stack is empty.
    if not ptr:
        while stack:
            temp = stack.pop()
            print(temp.data, end = " ")

    print()

# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    preorder_itr(root)
    preorder_itr_mod(root)
