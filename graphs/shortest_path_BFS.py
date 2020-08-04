# Program to find shortest path between the two nodes in the graph.
# Now, we know that BFS will give the shortest path in the graph due to its properties
# of LIFO used queue , that whoever are explored first, are searched first.
# This is true for only unweighted graph.
# The fact that BFS searches in the order of increasing levels , so that always when the
# first time node is discovered, it is the first time seen and thereby it is the shortest
# distance between the source and the nodes.
# -----------------------------------------------------------------------------
#                   2   4
#                    \ /
#          1          3 -- 5
#        /   \      /     /
#       0     8 -- 7 ---- 6
#        \   /  /  \
#          9   10--11
#
#
# -----------------------------------------------------------------------------

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

    # we apply BFS and stop as soon as we found the destination path
    def BFS_shortest(self, source, destination):

        queue = deque()
        visited = set()
        queue.append(source)
        visited.add(source)
        parent = [None] * self.V
        dist = [0] * self.V

        found = False
        while queue:

            curr = queue.popleft()
            for i in self.graph[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    parent[i] = curr
                    dist[i] = dist[curr] + 1
                    if i == destination:
                        found = True

            if found:
                break

        if not found:
            print("NO PATH !")

        else:
            # use the parent array to reconstruct the path from source
            curr = parent[destination]
            path = [destination]

            # this loop will always stop as parent[0] == None always
            temp = destination
            while curr:
                path.append(curr)
                destination = parent[destination]
                curr = parent[destination]

            # extra check for if it is the source vertex itself
            if source == 0:
                path.append(0)
            path = path[::-1]
            print(path)
            print(dist[temp])


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
    #graph.printGraph()
    graph.BFS_shortest(0, 10)
