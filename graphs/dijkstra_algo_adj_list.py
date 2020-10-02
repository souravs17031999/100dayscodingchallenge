# Program for computing the shortest path between source node to all nodes in the graph.
#
# So, how do we approach it ? - using greedy approach
# So, we we need to go from source node {0} -> {4}, and there are intermediate nodes {1}, {2}, {3}.
# Then, we need to get shortest distance for all intermediate nodes and that will give us overall shortest dist.
# That means there must be optimal subtructure property in the problem of finding shortest path.
# Steps in brief : 
# - Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
# - Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
# - For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. 
#   Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. 
#   For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has length 2, 
#   then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
# - When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. 
#   A visited node will never be checked again.
# - If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited 
#   set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. 
#   The algorithm has finished.
# - Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
# 
# We can use various DS for this algorithm.
# Here, we are computing shortest path only using PriorityQueue and there is no
# need of any decrease key functionality, logic is to simply keep only those nodes
# which are unprocessed and insert initially only the source node.
# RUNTIMES : 
# array (adj matrix) : 0(V^2) [due to linear time searching in extract-minimum operation]
# min-binary heap (prority-queue) + adj list : 0(V + E)log(V) / 0(E* log V) [efficient extract-minimum operation]
# More variants of binary heap can be used : Fibonacci heap, Self Balancing tree etc...

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
