# Program to print all the nodes which are at a given distance K (int) from a target node (ptr of type Node).
# IDEA: Now, the idea is to first observe that if we reach a target node, then we can go to kth level from
# there in the left and right subtree from there but the problem is that we are not able to go up and back
# and select those that are far up k distance away.
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# Like in above example, suppose target node is 2, and k = 1, then we can print "4", "5"
# but we will not be able to print "1" which is also at k = 1 distance.
# For that, we will have to keep a track of ancestors, "1", and give a call to right recursive call.
# Actually, we need to have a track of all the ancestors, and if target is on left side, then we need to make
# call on right.
# This call on right side will be for distance k - D - 2, D is left distance of target from ancestors (current root).
# But if target is on right subtree, then we need to call for left subtree for distance using all the ancestors.
# In this way, we will be able to print all the nodes at a distance k from the target node.
# There is one more interesting case, like in above case, when K > D, then it will be positive and we can make
# a call for other side of ancestor subtree.
# but there maybe some cases, when K  < D, and the value for K - D - 2 comes out to be -ve,
# so, at that point there is no need of any call for the other subtree of ancestor, but it is the ancestor itself
# which is to be printed, as it is K distance away.
# So, either we need to print the ancestors or call for right subtree.
# So, IF D + 1 == K, then it is the ancestor which is to be printed otherwise call for right subtree.
# Since, we are returning from the target node the value of D + 1 (return is necessary for backtracking to ancestors)
# so that's if D + 1 is exactly K distance, that means ancestors is the one which is to be printed,
# and no call for right subtree will be made.
# ------------------------------------------------------------
                   #         1
                   #       /  \
                   #      2    3
                   #    /  \
                   #   4    5
                   #  / \   / \
                   # 6   7  8  9
                   #    / \
                   #    10 11

# So, in the above tree, suppose the target is "4", and then k = 2,
# -------------------------------------------------------------
# SINCE, WE CAN SEE , WE ARE GOING TO TRAVERSE ALL THE NODES ONCE AND ATMOST TWICE.
# SO, TIME : 0(N).
# -----------------------------------------------------------------
# SECOND ITERATIVE APPROACH :
# Now, what we can do is use to extend the level order traversal BFS, So first of all once we reach target node, we have to also go back
# up to ancestors, so we are gonna have some link back upto the ancestor, so we create hashMap, for storing all parent nodes with the keys
# as the node value, and parent value as value.
# Using BFS, create this above said HashMap.
# NOW, we again START BFS from inserting the target node initially, and then do BFS in root.left, root.right, root.parent way.
# and also keep a track of distance covered from target node, and if this distance is equal to K, then we will be able to print all the
# nodes in the queue at that time.
# Doing BFS in left, right, parent is important as first we are ensuring that we are accounting for nodes that are k distance away from this
# target node in its own subtree, and then including parent means that after covering nodes in its own subtree, we are also going up the
# ancestor and then including their subtree , now obviously we also need to make sure that we donot traverse the already covered nodes again.
# For that, we can keep a visited [] which stores bool depending on whether that node is visited or not.
# In this way, all the nodes will be covered.
# PSEUDO CODE FOR ABOVE APPROACH :

# def BFSMAP(root):
#    TreeMap = {}
#    DO BFS AND store all the nodes as keys and their parent as values.
# def printKBFS(root, target, k, Treemap):
    # Initialize BFS queue with target node.
    # initalize dist = 0
    # visited = set()
    # Start BFS - while queue is not empty :
    #     if dist == k:
    #         print queue
    #
    #     n = len(queue)
    #     for i in N:
    #         curr = queue.popleft()
    #         call for curr.left, and check if not visited, insert into queue and set as well
    #         call for curr.right, and check if not visited, insert into queue and set as well
    #         call for curr.parent using hashMap, and check if not visited, insert into queue and set as well
    #
    #     dist += 1
# -----------------------------------------------------------------



class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque
# function for level order traversal for binary tree
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


# function to print kth level from the given root
def printKthLevel(root, k):
    if root == None:
        return

    if k == 1:
        print(root.data, end = " ")
        return

    printKthLevel(root.left, k - 1)
    printKthLevel(root.right, k - 1)

# Main function to print all nodes at k distance
def printKTree(root, target, k):

    if root == None:
        return -1  # it means we haven't found our target in this call.

    if root == target:
        printKthLevel(target, k)
        return 0  # returning 0 as the distance of this target node to its ancestor is 0.

    # so, now we check whether our target is in left node or right node
    Dl = printKTree(root.left, target, k)
    # if it is in left subtree of current root, then we need to check if there is requirement of calling
    # right subtree depending on whether D + 1 == k or not.
    if Dl != -1:
        # check whether ancestor itself is K distance away
        if Dl + 1 == k:
            print(root.data, end = " ")
        # otherwise go for right subtree first node as root and print all nodes at effective distance
        # that is K - 2 - DL
        else:
            printKthLevel(root.right, k - Dl - 2)

        return Dl + 1

    # similarly , we check for whether target is in our right subtree of current root
    Dr = printKTree(root.right, target, k)
    if Dr != -1:
        if Dr + 1 == k:
            print(root.data, end = " ")
        else:
            printKthLevel(root.left, k - Dr - 2)

        return Dr + 1

    # if target is neither in left subtree nor in right subtree
    return -1



# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    levelOrder(root)
    target, k = root.left, 1
    print()
    printKTree(root, target, k)
