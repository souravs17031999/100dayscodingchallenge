# Program to compute minimum spanning tree and cost for the graph given
# TIME : (E*log(V))
# Useful particulary for dense graphs,
# and kruskal's algo is good for sparse graphs.

from collections import defaultdict as dd
from heapq import heapify, heappush, heappop
import sys
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

    def compute_MST(self, source):

        cost = [None] * self.V
        parent = [None] * self.V
        visited = [None] * self.V

        p_queue = []
        heappush(p_queue, (0, source))

        for i in range(self.V):
            cost[i] = sys.maxsize

        cost[source] = 0

        while p_queue:

            u = heappop(p_queue)
            curr_node = u[1]
            visited[curr_node] = True

            for i in self.graph[curr_node]:
                v, weight = i[0], i[1]
                if not visited[v] and weight < cost[v]:
                    cost[v] = weight
                    parent[v] = u
                    heappush(p_queue, (cost[v], v))

        print(visited)
        print(parent)
        print(cost)

        for i in range(self.V):
            print(parent[i], i)


if __name__ == '__main__':

    graph = Graph(9)
    graph.add_Edge(0, 1, 4)
    graph.add_Edge(0, 7, 8)
    graph.add_Edge(1, 2, 8)
    graph.add_Edge(1, 7, 11)
    graph.add_Edge(2, 3, 7)
    graph.add_Edge(2, 8, 2)
    graph.add_Edge(2, 5, 4)
    graph.add_Edge(3, 4, 9)
    graph.add_Edge(3, 5, 14)
    graph.add_Edge(4, 5, 10)
    graph.add_Edge(5, 6, 2)
    graph.add_Edge(6, 7, 1)
    graph.add_Edge(6, 8, 6)
    graph.add_Edge(7, 8, 7)
    graph.printGraph()
    graph.compute_MST(0)
