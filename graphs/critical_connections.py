# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents 
# a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
#
# Return all critical connections in the network in any order.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
#        {2}
#       /  |
#   {1} \  |
#    |    {0}
#   {3}
# Here, 1-3 is critical connection.
#
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# This is very similar question to finding bridges in the graph.

from collections import defaultdict as dd 
class Solution:
    
    def __init__(self):
        self.timer = 0
    
    def dfs(self, u, visited, parent, low, disc, graph, res):
    
        visited[u]= True

        disc[u] = self.timer
        low[u] = self.timer
        self.timer += 1

        for v in graph[u]: 
            
            if not visited[v] : 
                parent[v] = u 
                self.dfs(v, visited, parent, low, disc, graph, res) 

                low[u] = min(low[u], low[v]) 


                if low[v] > disc[u]: 
                    res.append([u, v])


            elif v != parent[u]: 
                low[u] = min(low[u], disc[v]) 

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = dd(list)
    
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        nodes = n
        visited = [False] * nodes 
        disc = [float('inf')] * nodes 
        low = [float('inf')] * nodes 
        parent = [-1] * nodes 
        self.timer = 0
        res = []
        for i in range(nodes):
            if not visited[i]:
                self.dfs(i, visited, parent, low, disc, graph, res)
        
        return res 
