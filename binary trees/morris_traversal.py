# Program to traverse the tree in inorder ordering using morris-traversal algorithm.
# So, we should understand that both in-built stack (recursion) and explicit stacks
# are being used for traversals (DFS) so that we can get back to the previous node where we
# are currently at.
# Like in inorder, postorder both requires travelling down to the leftmost node and then
# back to previous node in different fashion (depending on which traversal it is).
# --------------------------------------
# So, here we have to traverse without using any stack (either in-built or explicit).
# For that, we devise a algo called morris traversal which says that at any current node ,
# if left node is not there, then we have to move right.
# But if left subtree exists, then we have to find the inorder predecessor, that means
# rightmost node of the left subtree and create a link back to the current node so that
# after traversing the complete left subtree, we can get back to the original current node
# and then start from there by moving to the right subtree for the current node.
# -----------------------------------------
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# ---------------------------------------------
# Now here, we first set our current ptr to root => "1", now, since left subtree exist,
# then, we find the inorder predecessor to be "5" and created the link link 5.right = 1
# and move the ptr to ptr.left
# again we do same as left subtree of "2" exists, so 4.right = 2.
# Now, since current ptr is at 4 and now left subtree don't exists, now
# we can print "4" and then move to ptr.right which will take us back to 2 (here is what that link helped us to get back to).
# Now, first we break this link created from 4 to 2 and then print "2", then move to its right sub tree where same will happen which happened to "5".
# Now, 5 will be printed , and we will move to it's right (again link will move us back to "1"),
# and now since right subtree of "1" exists, then we break the link, print the data "1" and
# move to it's right , that is 3, now again nothing exists in the left subtree of "3",
# therefore we print "3" and move to it's right, which is None, here our while loop stops.
# ----------------------------------------------------
# While current is not NULL
#    If the current does not have left child
#       * Print current’s data
#       * Go to the right, i.e., current = current->right
#    Else
#       * Make current as the right child of the rightmost
#          node in current's left subtree
#       * Go to this left child, i.e., current = current->left
# ---------------------------------------------------------
# TIME : 0(N), SPACE : 0(1) BECAUSE ALL EXTRA BACK LINKS/POINTERS CREATED ARE DESTROYED IN THE NEXT ITERATION ,
# SO NO EXTRA SPACE IS REQUIRED, AND ALSO TIME COMPLEXITY WILL BE 0(N), AS WE ARE VISITING ALL THE NODES AT MOST 2 TIMES.

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# function to do morris traversal
def morris_traverse(root):

    # if tree is empty
    if root == None:
        return

    # setting current ptr as root
    ptr = root
    # until the ptr is not None
    while ptr:

        # if left subtree not exists
        if not ptr.left:
            print(ptr.data, end = " ")
            ptr = ptr.right

        # if left subtree exists
        else:

            # find inorder predecessor in the left subtree, rightmost node
            pre = ptr.left
            while pre.right and pre.right != ptr:
                pre = pre.right

            # Now, if we have found that predecessor node, create that back link
            if not pre.right:
                pre.right = ptr
                ptr = ptr.left

            # if we traversed this new back link already, then break the link
            else:
                pre.right = None
                print(ptr.data, end = " ")
                ptr = ptr.right


# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #inorder_rec(root)
    morris_traverse(root)
