from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v, w):
        self.graph[u].append((v, w))

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

if __name__ == '__main__':

    graph = Graph(12)
    graph.add_Edge(0, 9, 1)
    graph.add_Edge(9, 8, 2)
    graph.add_Edge(8, 1, 3)
    graph.add_Edge(8, 7, 4)
    graph.add_Edge(7, 10, 5)
    graph.add_Edge(7, 3, 6)
    graph.add_Edge(10, 11, 7)
    graph.add_Edge(11, 7, 8)
    graph.add_Edge(3, 2, 9)
    graph.add_Edge(3, 4, 10)
    graph.add_Edge(3, 5, 11)
    graph.add_Edge(5, 6, 12)
    graph.add_Edge(6, 7, 12)
    graph.printGraph()
