# Program for printing left view of the tree
# TIME: 0(N) , space : 0(N) if using queue or if using stack for recursion

from collections import deque

class Node:
    """Node structure """
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def print_left_view(root):

    queue = deque()
    queue.append(root)
    queue.append(None)
    print(root.data, end = " ")

    while queue:

        curr = queue.popleft()
        if curr == None:
            if queue:
                queue.append(None)
                next = queue.popleft()
                print(next.data, end = " ")
                if next.left:
                    queue.append(next.left)
                if next.right:
                    queue.append(next.right)
        else:

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


def print_left_view_recr(root, level, max_level):

    if root  == None:
        return
    if max_level[0] < level:
        print(root.data, end = " ")
        max_level[0] = level

    print_left_view(root.left, level + 1, max_level)
    print_left_view(root.right, level + 1, max_level)

def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    # max_level is passed as reference as we donot want it to return to older value while backtracking
    print_left_view_recr(root, 1, [0])



# driver test function
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(9)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    print_left_view(root)
