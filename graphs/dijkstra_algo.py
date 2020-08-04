# Program to compute dijkstra algorithm to find the shortest distance to all the destination nodes from a source node.

# We apply Greedy approach at every point to get the minimum.
# This can be efficiently implemented using PriorityQueue but in python, decrease key is not given which is required
# while updating priorities.
# So, we have to write our own PriorityQueue class and also maintain mapping from nodes to curr index in the heap.
# and also update this mapping whenever there is any change in the position of the nodes.

# Otherwise, we can simply also use a set, and then find the minimum every time in linear time (which is greater than in minHeap-queue)
# But for simplicity, we can use it.
# So, everytime we calculate minimum based on the distances where stored item is a tuple (dist, value).
# Now, we remove it from the set, as set only contains unvisited vertex,
# Hence, now for every adjacent vertices, calculate and update the distance as required, also if the current pair is already in set,
# we remove it, and we insert the new pair with new distances.
# So, here we keep two extra pair of vertices, where array dist is used to store
# all the shortest distances at index "i" for all source to i nodes.
# and array prev contains previous node (parent) which can be used to reconstruct
# the distance.

# TIME : 0(V + E)log(V), V : VERTICES, E : EDGES, WHEN ADJACENCY LISTS
# TIME : O(V^2), WHEN ADJACENT MATRIX

import sys
from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = [[0 for column in range(size)] for row in range(size)]


    def printGraph(self):
        print(self.graph)

    def compute_shortest_path(self, source):

        dist = [None] * self.V
        prev = [None] * self.V
        dist[source] = 0

        # this set will be used to maintain the set of unvisited vertices
        p_queue = set()
        p_queue.add((0, source))

        for i in range(self.V):
            if i != source:
                dist[i] = sys.maxsize

        while p_queue:

            temp = min(p_queue)  # this is the main bottleneck, which has to be implemented using binary min heap/PriorityQueue
            p_queue.remove(temp)
            curr_node, curr_dist = temp[1], temp[0]

            for i in range(self.V):
                if self.graph[curr_node][i]:
                    alt = dist[curr_node] + self.graph[curr_node][i]
                    if alt < dist[i]:
                        dist[i] = alt
                        prev[i] = curr_node
                        if (i, dist[i]) in p_queue:
                            p_queue.remove((i, dist[i]))
                        p_queue.add((alt, i))

        print(dist)
        print(prev)


if __name__ == '__main__':

    graph = Graph(9)
    graph.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    graph.compute_shortest_path(0)
