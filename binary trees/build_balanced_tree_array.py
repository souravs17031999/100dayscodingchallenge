# Program for building balanced tree from the given array.
# IDEA: If we create a tree directly using the arrays elements, then mostly it will be
# sweked, and to make it balanced, we need to think in terms of log(N).
# so, we can actually apply DAC approach by computing the mid point and making it root
# and then recursively build from calling left sub tree and then buuilding from calling right sub tree.
# We can take example for follwoing tree and visualize stack call :
# let's take , arr = [1, 2, 3, 4, 5, 6, 7]
# So, mid is 4, then we go for building left subtree (1, 2, 3) and right subtree (5, 6, 7) with 4 as root.
# Then, mid is 2 and we create the tree with 2 as root , left subtree (1) and rightsubtree (3)
# Then, we return to the root - "2" and then we return to root "4", now, we call right side of root "4".
# Now, mid is 6 with 6 as root, left subtree (5) and right subtree (7).
# Finally, we retunr again to root "6" and then to root "4".
# Finally, we return this root as now start > end.
# --------------------------------
# BFS FOR ABOVE TREE WOULD LEAD TO  : 4 2 6 1 3 5 7
#                     4
#                   /  \
#                  2    6
#                /  \  /  \
#               1   3  5   7
# --------------------------------------
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

# main recursive function to build the balanced tree from array
def buildFromArray(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left =  buildFromArray(arr, start, mid - 1)
    root.right = buildFromArray(arr, mid + 1, end)

    return root

# driver test function
if __name__ == '__main__':
    arr, n = [1, 2, 3, 4, 5, 6, 7], 7
    root = buildFromArray(arr, 0, n - 1)
    levelOrder(root)
