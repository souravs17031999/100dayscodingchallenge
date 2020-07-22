# Program for printing kth level of binary tree
# Here, we can see it's top down approach, so either we can use BFS using queue or we can use
# recursive preorder top down traversal.
# BFS approach will go while queue is not empty, and for each level, we can check if we reached level
# = k and print the values for that level.
# TIME : 0(N), AS every node will be visited and it will be visited atmost twice.
# Now, Space : 0(W), w is width in worst case, it will be max number of nodes at bottom most
# of tree, thereby 2^(H-1).
# So, can we do better than this ?
# Yes, if we use recursive preorder traversal.
# If we have something like :
# printKthLevel(root, K), and we consider base cases, as if root becomes None, then return
# elif if K == 1, then we have reached that level, because in every recursive call now for
# left first, right then, we will go for  k - 1, reducing this level in every call for left subtrees
# first, then right subtrees.
# In this way, at any point, K == 1, we print that sepcific node.
# Here, we only visited all the nodes once.
# TIME : 0(N), SPACE : 0(N).
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

# RECURSIVE APPROACH OPTIMISED
def printKthLevel(root, k):
    if root == None:
        return

    if k == 1:
        print(root.data, end = " ")
        return

    printKthLevel(root.left, k - 1)
    printKthLevel(root.right, k - 1)

from collections import deque
# ITERATIVE BFS APPROACH
def printKthBFS(root, k):

    if not root:
        return

    queue = deque([])
    queue.append(root)
    level, flag = 0, False
    
    while queue:

        n = len(queue)

        for i in range(n):

            temp = queue.popleft()

            if level == k:
                flag = True
                print(temp.data, end = " ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        level += 1
        if flag:
            break

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printKthBFS(root, 0)
