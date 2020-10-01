# Program to detect cycle in directed and undirected graph .
# TIME : (O + V), SPACE : 0(V)

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

# UNIDRECTED GRAPH :
# For undirected graph, basically we are able to move to and fro (in both directions) for vertices
# and so if at any point we see node that is visited and that is not parent of current node,
# that means we detected a cycle and we can return True safely.
# Now, it may be possible that graph is disconnected, so in one of the graph cycle exists,
# and in one not, and if we just start from that graph then we are not able to find the cycle,
# so, we need to DO DFS for each vertex.
# Basically, if we are going in a DFS traversal and if we encounter a node that is already visited and it is also not the parent of current node, then it surely 
# means that we have visited this node earlier and this is due to cycle in the graph because otherwise only case that remains if not cycle is that if it parent of the node
# but since it's not parent so, we are meeting this node again after few calls that proves that we have a cycle in the graph.
# -----------------------------------------------------------------
    # modified DFS
    def DFS_undirected(self, v, visited, parent):

        visited.add(v)

        for i in range(self.V):
            if i not in visited:
                if self.DFS_undirected(i, visited, v):
                    return True

            elif i != parent:
                return True

        return False

    # wrapper function
    def is_cyclic_undirected(self):
        visited = set()
        # for every vertex, considering disconnected graphs
        for i in range(self.V):
            if i not in visited:
                if self.DFS_undirected(i, visited, -1):
                    return True

        return False
# ------------------------------------------------------

# DIRECTED GRAPH :
# Here, it is not necessary that node is visited again and is not a parent , then it is cycle
# Because it is directed so as we can see in the below example :
#
#
#    (0)  ----> 1
#     |      /^
#     ^    /
#    (2)
# as we can see, if we start from 0, this is not a cycle.
# Therefore, we need to maintain a set, which can contain recent added visited nodes
# for the current node DFS, and we need to push whenever we see a node in the current DFS
# and pop it from the this set when we don't see a cycle.
# ------------------------------------------------------------
    def DFS_directed(self, v, visited, recurStack):

        visited.add(v)
        recurStack.add(v)

        for i in range(self.V):
            if i not in visited:
                if self.DFS_directed(i, visited, recurStack):
                    return True

            elif i in recurStack:
                return True

        recurStack.remove(v)
        return False


    def is_cyclic_directed(self):
        visited = set()
        recurStack = set()

        # for all nodes due to disconnected graphs
        for i in range(self.V):
            if i not in visited:
                if self.DFS_directed(i, visited, recurStack):
                    return True

        return False


# ------------------------------------------------------------


# driver test function
if __name__ == '__main__':

    graph = Graph(4)
    graph.add_Edge(0, 1)
    graph.add_Edge(2, 0)
    graph.add_Edge(1, 2)
    graph.add_Edge(2, 3)
    # graph.printGraph()
    print(graph.is_cyclic_undirected())
