# Program to compute total connected components in the graph.
# So, components (or connected components) are all the disjoint subgraphs present in the
# super graph.
# So, this can be done easily by using BFS or DFS.
# We maintain a usual visited set, and this set contains all the elements being added in the
# traversal of the nodes, so we traverse for every node in the graph, and call BFS/DFS for each
# node, and so as soon as one component gets traversed, we get our those elemnets in visited set
# and so, next traversal will start from next unvisited set, and while doing all this, we also
# maintain a count variable which keeps counting how many times we do this BFS/DFS traversal.
# This count is total connected components in the graph.
# ---------------------------------------------------------------
#
#      1 -- 3          7        10    12     14 -- 15
#      |    |        /  \      / \  /       |      |
#      2 -- 4       5    8 -- 9   11        13 --  16
#                   \   /
#                    6
# ---------------------------------------------------------------
# In the above graph, we can see total connected components = 3.
# ------------------------------------------------------------------
# TIME : 0(E + V), SPACE : 0(V + E)
# ------------------------------------------------------------------


from collections import defaultdict as dd, deque
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

    def DFS(self, source, visited):

        visited.add(source)

        for i in self.graph[source]:
            if i not in visited:
                self.DFS(i, visited)

    def compute_component(self):
        visited = set()
        count = 0
        for i in range(1, self.V):
            if i not in visited:
                count += 1
                self.DFS(i, visited)
        return count

if __name__ == '__main__':

    graph = Graph(16)
    graph.add_Edge(1, 3)
    graph.add_Edge(1, 2)
    graph.add_Edge(2, 4)
    graph.add_Edge(3, 4)
    graph.add_Edge(7, 5)
    graph.add_Edge(5, 6)
    graph.add_Edge(6, 8)
    graph.add_Edge(11, 7)
    graph.add_Edge(7, 8)
    graph.add_Edge(8, 9)
    graph.add_Edge(9, 10)
    graph.add_Edge(10, 11)
    graph.add_Edge(11, 12)
    graph.add_Edge(13, 14)
    graph.add_Edge(14, 15)
    graph.add_Edge(15, 16)
    graph.add_Edge(16, 13)
    print(graph.compute_component())
