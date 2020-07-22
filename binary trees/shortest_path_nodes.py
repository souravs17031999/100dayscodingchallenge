# Program for finding the shortest path between nodes in a binary tree.
# Here, we can observe from the Tree that :
# Firstly, LCA is the first common ancestor that is lowest , this is also the
# point through which shortest distance path will go through.
# Now, DIST(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2 * Dist(root, LCA(n1, n2))
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# Let's say for DIST(4, 5) = 2
# This can be verfiied, Dist(root, 4) = 2 and Dist(root, 5) = 2
# Dist(root, LCA(n1, n2)) = 1
# So, it can be seen that 2 + 2 - 2 * 1 = 2 (Dist(4, 5))
# TIME : 0(N), SO OVERALL WE ARE PROCESSING EACH NODE AND ATMOST TWICE.
# ---------------------------------------------------------------
# IS THERE A BETTER WAY TO DO THIS ?
# ---------------------------------------------------------------
# Think about directly first computing LCA.
# Then, Dist(a, b) = Dist(a, LCA(a, b))  + Dist(b, LCA(a, b))

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def findPath(root, path, k):

    if root == None:
        return False


    path.append(root.data)
    if root.data == k:
        return True

    if root.left and findPath(root.left, path, k) or root.right and findPath(root.right, path, k):
        return True

    path.pop()
    return False

def findShortestPath(root, x, y):

    if root == None:
        return 0

    path1, path2 = [], []
    findPath(root, path1, x)
    findPath(root, path2, y)

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1

    return len(path1) + len(path2) - 2 * i

# SECOND APPROACH :


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(findShortestPath(root, 4, 3))
