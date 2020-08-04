# Here, we are computing shortest path only using PriorityQueue and there is no
# need of any decrease key functionality, logic is to simply keep only those nodes
# which are unprocessed and insert initially only the source node.

from collections import defaultdict as dd
from heapq import heapify, heappush, heappop
import sys

class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

    def compute_shortest_path(self, source):

        dist = [None] * self.V
        prev = [None] * self.V


        for i in range(self.V):
                dist[i] = sys.maxsize

        dist[source] = 0

        p_queue = []
        heappush(p_queue, (0, source))
        while p_queue:

            temp = heappop(p_queue)
            curr_node, curr_dist = temp[1], temp[0]
            for i in self.graph[curr_node]:
                v, weight = i[0], i[1]
                alt = dist[curr_node] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = curr_node
                    heappush(p_queue, (dist[v], v))

        print(dist)

if __name__ == '__main__':

    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
    g.printGraph()
    g.compute_shortest_path(0)
