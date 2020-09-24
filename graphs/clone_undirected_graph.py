# Like we have done in singly linked list copying with random pointers, likewise we are going to use hashmaps to apply the
# same algorithm.
# Traversing BFS + HashMap to indicate which nodes have been visited/cloned and also to keep mark of all
# adjacent nodes/neighbours in the adjacency list.
# TIME : 0(E + V)


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        queue = deque()
        map = {}

        if not node:
            return node

        queue.append(node)
        new_src = Node(node.val)
        map[node] = new_src

        while queue:

            curr = queue.popleft()

            for i in curr.neighbors:

                if i not in map:
                    new_node = Node(i.val)
                    map[i] = new_node
                    queue.append(i)

                map[curr].neighbors.append(map[i])

        return map[node]
