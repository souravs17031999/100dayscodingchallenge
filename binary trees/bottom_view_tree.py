# Program for printing bottom view of the tree.
# We can take example for follwoing tree :
#         (x)1
#          /  \
#  (x-1) 2     3 (x+1)
#       /  \
# (x-2)4    5(x)
# -----------------------------------------------------------------------------------------
# We need to include one horizontal distance in the structure node, and for every node "x", horizonal distance for left node
# is (x - 1) and for right node (x + 1).
# One thing to note is that all the bottom most nodes 2, 4, 5 are in sorted order (x-2, x, x+1)
# ------------------------------------------------------------------------------------------
# we can use simple BFS for traversal and also use a Hashmap which stores horizonal distance as key and node value as value.
# NOTE: This hashmap needs to be stored in sorted order on the key values.
# at the end, we will be having only the bottom most nodes in the map as we keep on updating the map with same horizonal dist.
# ------------------------------------------------------------------------------------------
#
#  (0)      20
#          /  \
#   (-1) 8    22 (+1)
#       /  \    \
# (-2) 5    3 (0) 25 (+2)
#         / \
#   (-1) 10  14 (+1)
# ------------------------------------------------------------------------------------------
# finally in the hashmap, all the keys will be storing distinct horizonal distanced values in sorted order.
# -------------------------------------------------------------------------------------------
# NOTE : SINCE PYTHON DOESN'T HAVE SORTED DICT (TREEMAP), SO WE HAVE TO MANUALLY SORT THE DICT AT THE LAST, SO TAKING 0(N*log(N))

from collections import deque
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.hd = 0

def print_bottom(root):

    if root == None:
        return

    queue = deque()
    Treemap = {}
    root.hd = 0
    queue.append(root)
    hd = 0
    while queue:

        curr = queue.popleft()

        hd = curr.hd

        Treemap[hd] = curr.data

        if curr.left:
            curr.left.hd = hd - 1
            queue.append(curr.left)

        if curr.right:
            curr.right.hd = hd + 1
            queue.append(curr.right)

    for i in sorted(Treemap.keys()):
        print(Treemap[i], end = " ")

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print_bottom(root)
