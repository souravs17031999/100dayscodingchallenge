# Program to compute strongly connected components in the graph.
# So, we have to understand that strongly connected components is a part of subgraph
# in which each vertex can be visited to itself while traversing in this component.
# For a strongly connected component to exist, there shouldn't be any node which can't be reached from any other node, that means every node should be reachable from every
# other node.
# In undirected graph, if the graph is connected then always it is undirected, it is only when graph is disconnected then we can have various strongly connected components.
# But in directed graph, there can be various different SCC in the same connnected graph like shown below :
#
#      1                    5 ___>6 
#     ^                     ^   /
#    /  \>                  | /
#   0 <__ 2 _____ > 3 ____> 4 <
#
# comp1 : 0, 1, 2
# comp2 : 3
# comp3 : 4, 5, 6
# ---------------------------------------------------------------------------------------------------------------------------
# So, if we will simply use BFS/DFS like in undirected graph, it will be inefficient, and so
# Firstly, we can think of using brute force approach that could be to apply floyd warshall and get all pairs shortest path, and if there exists inf between any two nodes, 
# that means there is no path between them and it cannot be strongly connected component otherwise it can be surely.
# But that will take 0(V^3) which is highly inefficient for bigger graphs (large number of nodes).
# Now, some observations : 
# => Reversing the graph won't change the SCC that means a graph which was strongly connnected won't change if we reverse the graph (transpose of graph).
# => Direction between componenets will reverse and so, while earlier we were able to move to all the vertices due to SCC property of graph, now we won't be able to move 
# from one SCC to another SCC and so we have to manually jump to different SCC and we can count how many jumps we took to cover all SCC, in this way Kosaraju's algo works.
#
#   SCC1 ->  SCC2 -> SCC3 (GRAPH)
#   SCC3 <- SCC2 <- SCC1  (TRANSPOSE OF GRAPH)
#   
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
            if curr not in visited:
                g.DFS(curr, visited)
                print()

if __name__ == '__main__':

    g = Graph(5)
    g.add_Edge(1, 0)
    g.add_Edge(0, 2)
    g.add_Edge(2, 1)
    g.add_Edge(0, 3)
    g.add_Edge(3, 4)
    g.compute_component()
