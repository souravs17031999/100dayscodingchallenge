# Program for computing minimum number of operations to make network connected.
# There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where 
# connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
# Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected 
# computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 
#
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
#
#      {0} ---- {1}              {0} ---- {1}
#       |   /               =>   |         |
#      {2}         {3}           {2}       {3}
# 
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Logic is to use concept of MST that if we have N number of vertices, then it is possible to reach all nodes using only N - 1 edges.
# But that is true for only single component graphs, and if we want to reach every node in multi-component generalised graphs, then we need to remove some redundant edges 
# and use it to connect to these compoenents.
# So, we need to calculate these redundant edges in the graphs, which are those edges whose removal doesn;t have any effect on number of compoenents of that specific subgraph.
# So, total redundant edges  = total_edges - ((N-1) - (compoenent - 1))
# And now if redundant edges >= compoenent - 1, then it is possible to connnect all these compoenent together, which is to remove compoenent - 1 edges and use it to join them.
# Otherwise, it's not possible to join them.

# TIME : 0(E + V)
# ------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict as dd

class Solution:
    
    def dfs(self, source, visited, graph):
        visited.add(source)
        for i in graph[source]:
            if i not in visited:
                self.dfs(i, visited, graph)
            
    def compute_comp(self, nodes, graph):
        count = 0
        visited = set()
        for i in range(nodes):
            if i not in visited:
                count += 1
                self.dfs(i, visited, graph)

        return count

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        graph = dd(list)
        total_edges = 0
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            total_edges += 1

        nodes = n
        if total_edges < n - 1:
            return -1

        comp = self.compute_comp(nodes, graph)
        r_edges = total_edges - ((n - 1) - (comp - 1))
        if r_edges < comp - 1:
            return -1

        return comp - 1
