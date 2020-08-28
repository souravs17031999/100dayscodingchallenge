# program for computing the diameter of the tree.
# Now, diameter is the maximum of the distance between two leaves.
# So, we have already seen other solutions for the problem and also observed how we are processing the nodes again and again once while computing the
# height and again while computing the diameter of individual node and then getting the max, thus making complexity 0(N^2).
# We have also seen bottom up approach in 0(N).
# Now, we will understand the use of DP in trees as we can see we can store the height of nodes and then use it to compute diameter of all the subtrees
# left and right and get the max of it without computing the height again for other subtrees.
# This will also be the general syntax for DP on trees.
# TIME : 0(N)

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# DP using postorder traversal

def diameter(root, res):

    if root == None:
        return 0

    left = diameter(root.left, res)
    right = diameter(root.right, res)

    temp = 1 + max(left, right)   # this case is when root is not part of answer and it will be passed onto above parent who called it
    ans = max(temp, 1 + left + right)  # this will be when root is part of answer
    res[0] = max(temp, ans)  # we have to take max of both possible above cases

    return temp

# res is passed as reference and will contain the final answer
def compute_diameter(root):
    res = [-sys.maxsize-1]
    diameter(root, res)
    return res[0]



import sys
# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(compute_diameter(root))
