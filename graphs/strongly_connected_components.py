# Program to compute strongly connected components in the graph.
# So, we have to understand that strongly connected components is a part of subgraph
# in which each vertex can be visited to itself while traversing in this component.
# So, if we will simply use BFS/DFS like in undirected graph, it will be inefficient, and so
# here, we will be using efficient algorithm : Kosaraju's algorithm.
# * We will firstly do DFS for each vertex while maintaining visited set, and maintain a extra stack to maintain
# order in order of exit times. So, last node visited should be first , so LIFO ordering with stack will be used.
# * Now, we transpose the graph, and then again do DFS for each of the vertex but now in the order of stack
# elements being popped off.
# Simply maintain count of how many times traversals will be done this second time.
# return the count of this counter variable.
# TIME : 0(V + E), SPACE : 0(V + E)

from collections import defaultdict as dd, deque
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):

        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

    def print_graph(self):

        for i in range(self.V):
            print(i, end = "->")
            for j in g[i]:
                print(j, end = " ")
            print()



    def DFS_mod(self, source, visited, stack):

        visited.add(source)

        for i in self.graph[source]:
            if i not in visited:
                self.DFS_mod(i, visited, stack)

        stack.append(source)

    def transpose_graph(self):
        
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_Edge(j, i)

        return g


    def DFS(self, source, visited):

        visited.add(source)
        print(source, end = " ")
        for i in self.graph[source]:
            if i not in visited:
                self.DFS(i, visited)


    def compute_component(self):

        visited = set()
        stack = deque()
        for i in range(self.V):
            if i not in visited:
                self.DFS_mod(i, visited, stack)

        g = self.transpose_graph()
        print(visited)
        print(stack)
        visited = set()
        while stack:
            curr = stack.pop()
            if i not in visited:
                g.DFS(i, visited)
                print()

if __name__ == '__main__':

    g = Graph(5)
    g.add_Edge(1, 0)
    g.add_Edge(0, 2)
    g.add_Edge(2, 1)
    g.add_Edge(0, 3)
    g.add_Edge(3, 4)
    g.compute_component()
