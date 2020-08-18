# Program for level order spiral traversal for the given binary tree.
# ----------------------------------------------------------------------------
#            1
#          /  \
#        2     3
#       /  \
#      4    5
#
# 1 2 3 5 4
# At each level, alternate levels are printed  first in same order, opposite order
# ----------------------------------------------------------------------------
# TIME : 0(N), SPACE : 0(N)

from collections import deque

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# METHOD 1 : USING TWO STACKS (OR ONE QUEUE AND ONE STACK)
def level_order_spiral(root):

    if root == None:
        return

    stack1, stack2 = deque(), deque()
    stack1.append(root)
    while stack1 or stack2:

        while stack1:
            top1 = stack1.pop()
            print(top1.data, end = " ")
            if top1.right:
                stack2.append(top1.right)
            if top1.left:
                stack2.append(top1.left)

        while stack2:
            top2 = stack2.pop()
            print(top2.data, end = " ")
            if top2.left:
                stack1.append(top2.left)
            if top2.right:
                stack1.append(top2.right)

# METHOD 2: USING DEQUE
# ------------------------------------------------------------------------

def level_order_deque(root):

    Deque = deque()
    Deque.append(root)
    direct = 0 # 0 means right to left, each time it is reversed
    while Deque:

        n = len(Deque)
        for i in range(n):

            if direct == 0:
                curr = Deque.pop()
                print(curr.data, end = " ")

                if curr.right:
                    Deque.appendleft(curr.left)
                if curr.left:
                    Deque.appendleft(curr.right)
            else:
                curr = Deque.popleft()
                print(curr.data, end = " ")
                if curr.left:
                    Deque.append(curr.left)
                if curr.right:
                    Deque.append(curr.right)

        direct = not direct

if __name__ == '__main__':
    root = Node(10);
    root.left = Node(20);
    root.right = Node(30);
    root.left.left = Node(40);
    root.left.right = Node(60);
    level_order_deque(root)
