# Program for computing minimum vertex cover for the binary tree.
# Vertex cover is the subset of vertices such that for every edge (u, v) either u is in vertex cover or v is in vertex cover.
# Although the name is Vertex Cover, the set covers all edges of the given graph.
# For graph it is NP-Complete, but for tree it is solvable.
# -------------------------------------------------------------------------------------------------------------------
#
#                  10
#                 /  \
#               20*    30*
#              /  \     \
#             40   50*    60
#                  / \
#                 70  80
#
# Simply stated, minimum vertices that can cover all the edges of trees.
# -------------------------------------------------------------------------------------------
# TIME : EXponential time complexity, due to overlapping subproblems.
# Applying DP on trees requires adding additional information in the structure of nodes of trees.
# This should help us in identifying if the problem is already solved, otherwise don't solve.

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.vc = 0

def vcover(root):

    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0

    if root.vc != 0:
        return root.vc

    size_incl = 1 + vcover(root.left) + vcover(root.right)

    size_excl = 0
    if root.left:
        size_excl += 1 + vcover(root.left.left) + vcover(root.left.right)
    if root.right:
        size_excl += 1 + vcover(root.right.left) + vcover(root.right.right)

    root.vc = min(size_incl, size_excl)

    return root.vc

# There is also DP solution which is more efficient discussed in DP section.

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.right.right = Node(60)
    root.left.right = Node(50)
    root.left.right.left = Node(70)
    root.left.right.right = Node(80)
    print(vcover(root))
