# Program to find the least common ancestor (LCA) that is the lowest possible node
# which is the ancestor for both the given nodes say x and y.
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
# Here, LCA(5, 3) = 1, this is the point they will meet for the first time,
# or this is the shortest distance between them.
# Again this problem is a top down approach, so preorder type of traversal is
# required.
# APPROACH :
# One simple approach, would be to basically store the path from root to given node x
# and then store the path from root to given node y.
# Then, we traverse both arrays, and find the first point where they don't match,
# as the prefix should match till somepoint, the point they start differe, is the LCA.
# ------------------------------------------------------------------------------------
# TIME : 0(N), SPACE IS 0(H), H IS HEIGHT OF TREE, WORST CASE IN SKWEDED TREE.
# CAN WE DO BETTER THAN THIS in terms of space efficiency (practical runtime)?
# -----------------------------------------------------------------------------------
# KEY OBSERVATION : the given nodes x, y will always be on the opposite side of LCA
# and for the given node itself is always the LCA.
# They can never be on same side.
# It means we can search for some x on one side, and then search for some y on other side.
# IF THEY both exist, then we found the LCA.
# So, we can write recursive function to get LCA like shown below.

def LCA(root, x, y):

    if root == None:
        return None

    if root.data == x or root.data == y:
        return root

    leftans = LCA(root.left, x, y)
    rightans = LCA(root.right, x, y)

    if leftans != None and rightans != None:
        return root

    # This case is important, as let's say we search for x in left subtree and couldn't find anything, so it
    # will return None, but if y is in rihgtpart of tree, then we should reutnr rightans and similarly for leftans
    if leftans != None:
        return leftans
    else:
        return rightans
