# program for counting and getting sum of all the nodes in the binary tree.
# Logic is simply to traverse the tree going to all the nodes once, for each
# counting as well as sum.
# Any traversal could be used, but we can surely use preorder traversal.
# Recurrence relation count : count(root) = 1 + count(root.left) + count(root.right)
# Recurrence relation sum : sum(root) = root.data + count(root.left) + count(root.right)
# ------------------------------------------------------------
# We can take example for follwoing tree and visualize stack call :
#       (1 + 3 + 1)  1
#                  /  \
#  (1+ 1 + 1)     2     3  (1 + 0 + 0)
#               /  \
# (1 + 0 + 0) 4    5 (1 + 0 + 0)
# AS WE CAN SEE, AT THE ROOT IT WILL BE RETURNED WITH VALUE OF "5".
# SAME IS THE CASE WITH THE SUM OF NODES, INSTEAD OF NUMBER, IT WILL BE PTR.DATA.
# ------------------------------------------------------------
# TIME : 0(N), SPACE : 0(1).

class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# function to count the nodes
def count_node(root):

    if root == None:
        return 0

    return 1 + count_node(root.left) + count_node(root.right)

# function to sum up the nodes
def sum_node(root):

    if root == None:
        return 0

    return root.data + sum_node(root.left) + sum_node(root.right)

# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(count_node(root))
    print(sum_node(root))
