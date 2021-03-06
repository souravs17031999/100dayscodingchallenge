# Program for DFS traversal for the given graph.
# We have already discussed we can use stack for this purpose , as whole purpose is
# to move and start from one node and go till it can go nowhere, and then backtrack
# and check if there is anymore path to go, and keeping on with this we can traverse
# all the paths , but we also have to maintain a visited set to ensure we are not
# covering the same node again.

from collections import defaultdict as dd, deque
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in range(self.V):
            print(i, end = " -> ")
            for j in self.graph[i]:
                print(j, end = ", ")
            print()

    def DFSUtil(self, source, visited):

        visited.add(source)
        print(source, end = " ")

        for i in self.graph[source]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self, source):
        visited = set()
        self.DFSUtil(source, visited)

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
    print("DFS : ")
    graph.DFS(0)
