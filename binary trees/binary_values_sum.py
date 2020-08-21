# Program to sum the overall nodes of binary trees given only binary values 0 or 1 where
# from root to leaf, it is in most signifant digits.
# EX.
#
#                 1
#               /  \
#              0    1
#             / \   /\
#            0   1 0  1
#
# We can see overall sum = 100 + 101 + 110 + 111 => 22
# -------------------------------------------------------------------------------------------
# It is simply topdown preorder traversal but how do we get the sum in one go and along with that
# we should not be required to again sum from root to leaf ?
# So, we can get away with having to again get the sum of root to leaf for some another path using bitwise trick.
# Using bitwise trick : 1->1 => 3 ; curr_number = (1 << 1) | 1 = 3
# So, we have to use stack for preorder traversal and while maintaing the stack we can actually use tupled data to store onto stack
# in which first index is root (node addr), and second index is running_sum and once we pop the node, we also pop the node value (bit value)
# this will enable us to get the running sum for another path without traversing back from root to leaf for another path.
# --------------------------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)

from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Node) -> int:
        stack = deque()
        total_sum = 0
        stack.append((root, 0))

        while stack:
            root, curr = stack.pop()
            curr = (curr << 1) | root.val
            if not root.left and not root.right:
                total_sum += curr
            if root.right:
                stack.append((root.right, curr))
            if root.left:
                stack.append((root.left, curr))
        return total_sum


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(0)
    root.right = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(1)
    s = Solution()
    print(s.sumRootToLeaf(root))
