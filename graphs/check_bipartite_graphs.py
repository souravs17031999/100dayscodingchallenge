# Program for checking if given graph is bipartite or not.
# NOTE : bipartite graphs are in which all the vertices can be grouped into exactly two sets such that no vertex of same
# set have edge between them.
# In other words, it can be explained in the m-colouring problem where m = 2, that is bipartite graphs should be 2 colourable.
# ------------------------------------------------------------------------------------------------------------------------------
# The algorithm will be simply to color the graphs vertices as they are explored in the following manner :
# We color the first unassigned vertex color "1", and now all neighbours the oppposite color "0"
# When we visit at any point already assingned vertex and the color for any of its negihbours matches its own color,
# then that graph will not be bipartite otherwise if all the colouring is possible , then it's bipartite.
# We use BFS for the above problem (although DFS can also be used) !
# ---------------------------------------------------------------------------------------------------------------------
# TIME : 0(V + E)

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

    def is_bipartite(self, src):

        queue = deque()
        queue.append(src)
        self.color[src] = 0
        while queue:

            curr = queue.popleft()

            for i in self.graph[curr]:
                if self.color[i] == -1:
                    self.color[i] = self.color[curr] ^ 1 # if it's already 0, then it will make it 1, if it's already 1, then it will be 0
                    queue.append(i)
                else:
                    if self.color[curr] == self.color[i]:
                        return False

        return True

    def check_bipartite(self):

        self.color = [-1] * self.V
        for i in range(self.V):
            if self.color[i] == -1:
                print(self.color)
                if not self.is_bipartite(i):
                    return False
        return True

if __name__ == '__main__':

    graph = Graph(4)
    graph.add_Edge(0, 1)
    graph.add_Edge(0, 3)
    graph.add_Edge(1, 2)
    graph.add_Edge(2, 3)
    graph.add_Edge(0, 2)
    graph.printGraph()
    print(graph.check_bipartite())
