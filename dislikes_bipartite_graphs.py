# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
# This problem can be solved using bipartite graphs.
# -----------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(E + V)

from collections import defaultdict as dd, deque 

class Solution:
    
    def BFS(self, source, color, graph):
        queue = deque()
        queue.append(source)
        color[source] = 0
        
        while queue:
            
            curr = queue.popleft()
            for i in graph[curr]:
                if color[i] == -1:
                    color[i] = color[curr] ^ 1
                    queue.append(i)
                else:
                    if color[curr] == color[i]:
                        return False
        return True
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = dd(list)        
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        color = [-1] * (N + 1)
        for i in range(1, N + 1):
            if color[i] == -1:
                if not self.BFS(i, color, graph):
                    return False
        
        return True
        
        
