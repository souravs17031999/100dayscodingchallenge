# Program for BFS traversals.
# We have already discussed how we can't only use queue just like in binary tree as graph contains cycles.
# So, we will also use a hashmap (set) to mark visited nodes.

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

    def BFS(self, source):

        if source not in self.graph:
            print("Source Vertex not present in Graph !")
            return

        queue = deque()
        visited = set()
        queue.append(source)
        visited.add(source)
        while queue:
            curr = queue.popleft()
            print(curr, end = " ")
            for i in self.graph[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


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
    # graph.printGraph()
    graph.BFS(0)
