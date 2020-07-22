# Program to find the diameter of the given binary tree.
# IDEA: Firstly, we need to observe one important thing is that , diameter of the binary tree will always be the maximum of three things :
# * diameter of left subtree
# * diameter of right subtree
# * length of leftmost end to rightmost end through root (h1 + h2), h1 is height of left subtree , h2 is height of right subtree.
# We can also observe from following trees :
# -------------------------------------------------------------------------------------------------------------------------------
#                     *                                       *                                                      *
#                   *   *                                   *    *                                                *     *
#                 *       *                              *    *    *                                           *   *  *    *
#               *   *                                      *   *     *                                       *     * *       *
#           *    *   *                                 *    *     *    *                                   *        *         *
#       *    *        *                             *    *   * *         *                               *                     *
#    *    *      *       *                        *   *                   *
#                                               *   *    *
#   diameter is diameter of left subtree (8)        diameter is diameter of right subtree (11)              diameter is longest path through root (10)
# --------------------------------------------------------------------------------------------------------------------------------
# We can take example for follwoing tree and visualize stack call :
#                   (2, 0, 3)  1
#                            /  \
#                  (0,0,2) 2     3  (0, 0, 0)
#                         /  \
#             (0, 0, 0)  4    5 (0, 0, 0)
# AT THE ROOT, MAX OF (2, 0, 3) WHICH IS 3 THAT IS THROUGH THE ROOT PATH WILL BE CHOSEN HERE AS diameter OF THE binary TREE GIVEN.
# ---------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(N^2), as we are going for every node while calculating diamter and while inside that diamter calculation, we also calculate height through
# recursion which can again take us to atmost n number of node.
# SPACE : 0(N).
# NOTE: SOMETIMES, THROUGH ROOT CAN BE DEFINED AS H1 + H2, OR SOMETIMES WE CAN DEFINE IT AS H1 + H2 + 1, THAT'S A THING TO NOTICE IN THE QUESTION.
# ALSO, POINT TO NOTE IS THAT HERE WE ARE FOLLOWING PREORDER TRAVERSAL.
# -----------------------------------------------------------------------------------
# CAN WE DO BETTER THAN THIS ?
# YES, WE CAN OPTIMIZE BY doing postorder traversal, that is bottom up traversal, this means that Now, at any node from bottom to top, we can return two values,
# height and diameter, and in this way, we can move up and return these two values up to the root.
# THIS WILL REDUCE THE TIME : 0(N), SPACE : 0(N).
# -----------------------------------------------------------------------------------

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# first approach for computing height and diameter of the binary tree.
def height(root):

    if root == None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def diameter(root):

    if root == None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight, max(ldiameter, rdiameter))

# tuple pair for use in saving height, diameter for every node
class Pair:

    def __init__(self):
        self.height = 0
        self.diameter = 0

# --------------------------------------------
# SECOND APPROACH OPTIMIZED TO 0(N) USING POSTORDER TRAVERSAL, BOTTOM UP APPROACH
# --------------------------------------------
def fastDiameter(root):
    p = Pair()

    if root == None:
        p.height = p.diameter = 0
        return p

    left = fastDiameter(root.left)
    right = fastDiameter(root.right)

    p.height = max(left.height, right.height) + 1
    p.diameter = max(left.height + right.height, max(left.diameter, right.diameter))

    return p

# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(diameter(root))
    print(fastDiameter(root).height)
    print(fastDiameter(root).diameter)
