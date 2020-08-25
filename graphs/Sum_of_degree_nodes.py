# Program for sum of degree of nodes in the graph.
# We know that if there are no edges in the graph, then sum  = 0
# Now, if we add one more edge, then we increase the degree by 1 for each node.
# Hence, total sum increases by 2.
# Thus, total sum of degrees = 2 * edges

from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

if __name__ == '__main__':

    graph = Graph(12)
    graph.add_Edge(0, 9)
    graph.add_Edge(9, 8)
    graph.add_Edge(8, 1)
    graph.add_Edge(8, 7)
    graph.add_Edge(7, 10)
    graph.add_Edge(7, 3)
    graph.add_Edge(10, 11)
    graph.add_Edge(11, 7)
    graph.add_Edge(3, 2)
    graph.add_Edge(3, 4)
    graph.add_Edge(3, 5)
    graph.add_Edge(5, 6)
    graph.add_Edge(6, 7)
    graph.printGraph()
