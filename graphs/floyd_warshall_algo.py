# Program to find the shortest distance for all pairs of source-destination paths.

# ----------------------------------------------------------------------------
# This is only efficient for small graphs due to its high complexity.
# Useful for graph representation in grid.
# TIME : 0(N^3) , so can be used till size of graph is around 100 nodes.
# ----------------------------------------------------------------------------
#
#            3<------------
#          /              \
#        0   ---> 1--> 2     2
#        \          /^
#          ----6 --
#
# So, the intial matrix will be something like below : (considering weights given)
#   [0, 3, 6, 15]
#   [inf, 0, -2, inf]
#   [inf, inf, 0, 2]
#   [1, inf, inf, 0]
# so, we can see initial there is no edge between 3 and 1.
# but after applying the algorithm , mat[3][1] = 4, because there is a path from 3 to 1 via 0 (considering weights given)
# --------------------------------------------------------------------------------------
# So, the logic of the algo is to check everytime for each of the vertices, if there is any shortest path possible via any other path
# and this is done for every possible pair of path, and so it takes 0(V^3).
# -----------------------------------------------------------------------------------------
# This is also useful for detecting negative weight cycle, if the values at the diagonal of the matrix (originally 0) meaning distance from itself to itself, are all
# negative numbers, then there is a negative weight cycle in the graph.
# -----------------------------------------------------------------------------------------
# DP ON GRAPHS.
#
# {0} ----- {3}                   [0, 3, inf, 5]
# ||    /     |                   [2, 0, inf, 8]
# || /        |                   [inf, 1, 0, inf] 
# {1} ------{2}                   [inf, inf, 2, 0]
#
# Now, here four nodes are present, so total 4 times we will fill this matrix and compute distances.
# First time, we will include 0, so now all the distances from 0 will be same, but now other distances will computed again by including 0 in its path :
# like earlier, d[1][2] = min(d[1][2], d[1][0] + d[0][2]) => inf (no changed)
# simi., d[1][3] = min(d[1][3], d[1][0] + d[0][3]) => 7 (changed from 8)
# sim. other values will be filled.
# Then, we will include 1, then fill all other values, sim. for 2, and 3 nodes.
# ------------------------------------------------------------------------------------------------------------------------------

import sys
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = [[0 for column in range(size)] for row in range(size)]


    def printGraph(self):
        print(self.graph)

    def compute_all_shortest(self):

        adj = [[sys.maxsize for column in range(self.V)] for row in range(self.V)]

        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 0:
                    adj[i][j] == sys.maxsize
                else:
                    adj[i][j] = self.graph[i][j]

        for i in range(self.V):
            adj[i][i] = 0

        # middle is the via node, left and right denotes all pairs of source-destination nodes.
        for middle in range(self.V):
            for left in range(self.V):
                for right in range(self.V):
                    adj[left][right] = min(adj[left][right], adj[left][middle] + adj[middle][right])

        print(adj)

        for i in range(self.V):
            if adj[i][i] < 0:
                print("NEGATIVE CYCLES DETECTED !")

if __name__ == '__main__':

    graph = Graph(9)
    graph.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    graph.compute_all_shortest()
