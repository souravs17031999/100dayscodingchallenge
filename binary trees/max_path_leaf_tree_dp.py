# Program for computing max path sum from leaf to leaf nodes.
# We have already seen other solutions to the problem but here we will use DP.
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# DP using postorder traversal

def path_sum(root, res):

    if root == None:
        return 0

    left = path_sum(root.left, res)
    right = path_sum(root.right, res)

    temp = root.data + max(left, right)  # this case is when root is not part of answer and it will be passed onto above parent who called it now here since
    # if this is leaf node, then we can simply ignore the subtrees if they contain negative values and return just the root value which is as below
    if not root.left and not root.right:
        temp = max(temp, root.data)
    ans = max(temp, root.data + left + right)  # this will be when root is part of answer
    res[0] = max(temp, ans)  # we have to take max of both possible above cases

    return temp

# res is passed as reference and will contain the final answer
def compute_max_sum(root):
    res = [-sys.maxsize-1]
    path_sum(root, res)
    return res[0]



import sys
# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(compute_max_sum(root))
