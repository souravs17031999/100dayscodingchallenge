# Print all the cycles in the undirected graph , individual cycles print on separated lines.
# ----------------------------------------------------------------------------------------------------
# Intuition is to do apply color traversal and mark the nodes as one of the vertices.
# WHITE (0) : NOT EXPLORED / VISITED
# GRAY (1) : PROCESSED BUT NOT FULLY EXPLORED
# BLACK (2) : FULLY EXPLORED
# So, intially everything is White, and hence all the nodes are unvisited.
# Now, we mark the node as gray, when first explored to indicate it is being PROCESSED, and go for its DFS and while DFS,
# If at any point, we encounter a node that is already in PROCESSED state, that means we found a cycle and we can increment
# cyclenumber and this "cyclenumber" is important as it will be used to mark the nodes of same cycles with unique same colors (or denoted by numbers).
# Then, once we found a cycle, we need to backtrack using parent pointers (stored in the some another array), and mark all those with same colors.
# Now, when we finish with this node's DFS, we mark it as Black to indicate we have completely processed this node.
# Similarly for all the nodes will be done and cycles will be marked with unique numbers as during each cycle detection, we increment cyclenumber.
# ----------------------------------------------------------------------------------------------------------
# TIME : 0(V + E), V FOR VERTICES, E FOR EDGES 

from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for i in range(1, self.V + 1):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

    def print_cycles_graph(self, u, v, color, mark, parent, cyclenumber):

        if color[u] == 2:
            return

        if color[u] == 1:
            cyclenumber[0] += 1
            cur = v
            mark[cur] = cyclenumber[0]

            while cur != u :
                cur = parent[cur]
                mark[cur] = cyclenumber[0]

            return

        color[u] = 1
        parent[u] = v

        for i in self.graph[u]:
            if i == parent[u]:
                continue
            self.print_cycles_graph(i, u, color, mark, parent, cyclenumber)

        color[u] = 2

    def cycles_helper(self, u, v, color, mark, parent):

        cyclenumber = [0]
        self.print_cycles_graph(u, v, color, mark, parent, cyclenumber)
        if cyclenumber[0] == 0:
            print("NO CYCLE DETECED !")
        else:
            print(f"CYCLE DETECTED : {cyclenumber[0]}")

        cycle_nodes = dd(list)
        for i in self.graph:
            if mark[i] != 0:
                cycle_nodes[mark[i]].append(i)

        for i in cycle_nodes:
            print(f"CYCLE : {i}", end = " ")
            print(cycle_nodes[i])

# driver test function
if __name__ == '__main__':

    N = 14
    graph = Graph(13)
    graph.add_Edge(1, 2)
    graph.add_Edge(2, 3)
    graph.add_Edge(3, 4)
    graph.add_Edge(3, 5)
    graph.add_Edge(4, 6)
    graph.add_Edge(5, 6)
    graph.add_Edge(5, 9)
    graph.add_Edge(4, 7)
    graph.add_Edge(7, 8)
    graph.add_Edge(6, 10)
    graph.add_Edge(10, 11)
    graph.add_Edge(11, 12)
    graph.add_Edge(12, 13)
    graph.add_Edge(11, 13)
    #graph.printGraph()
    color = [0] * N
    mark = [0] * N
    parent = [0] * N
    graph.cycles_helper(1, 0, color, mark, parent)
