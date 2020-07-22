# Program to check if the given binary tree is height balanced or not.
# Height Balanced Tree means for every node difference bewteen height of left subtree and right subtree should be atmost 1.
# If height of left sub tree is h1, if height of right sub tree is h2, then at every node, |h1 - h2| <= 1.
# IDEA: so, logic is to simply we can get height of left subtree and right subtree at every node using postorder traversal.
# So, basically we can get something like :
# def isBalanced(root):
#        if root == None:
#            return True
#    lheight, rheight = isBalanced(root.left), isBalanced(root.right)
#    then , we can check here, if abs(lheight - rheight) <= 1 and isBalanced(root.left) and isBalanced(root.right):
#        return True
# otherwise finally return False
# This would take upto 0(N^2) and SPACE : 0(N).
# ---------------------------------------------------------
# So, can we do better than this ?
# Yes, we can follow bottom up approach and return a tuple containing (height at that node, True/False based on if balanced or not).
# In this way, we can move till upto root, which will return if tree is height balanced or not.
# BELOW CODE IS FOR THIS OPTIMIZED APPROACH :
# TIME : 0(N), SPACE : 0(N).
# ------------------------------------------------------------
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
# tuple pair for use in saving height, diameter for every node
class Pair:

    def __init__(self):
        self.height = 0
        self.balance = True

# recursive approach for postorder traversal and using above tuple to return whether tree is height balanced.
def isBalanced(root):

    p = Pair()

    if root == None:

        p.height = 0
        p.balance = True
        return p

    left = isBalanced(root.left)
    right = isBalanced(root.right)

    p.height = max(left.height, right.height)  + 1

    if abs(left.height - right.height) <= 1 and left.balance and right.balance:
        p.balance = True

    else:
        p.balance = False

    return p

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(isBalanced(root).balance)
