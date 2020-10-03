# Program to compute network delay for the entire network.
# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), 
# where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
# 
#            1
#     {1} <----- {2}
#                 |   1
#     {4} <----- {3}
#            1  
#
# We will apply dijsktra algorithm for this to compute all nodes distance from a single source given as per the question and get the maximum distance possible to any node as 
# that will be the shortest distance possible for the farthest node, which is what network delay is.
# TIME: (N * log(N)), where N are the number of nodes in the graph.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict as dd, deque
from heapq import heapify, heappush, heappop
import sys 
class Solution:
    
    def dijsktra_dist(self, source, dist, graph):
        
        p_queue = []
        dist[source] = 0
        heappush(p_queue, (0, source))
        
        while p_queue:
            curr_dist, curr_node = heappop(p_queue)
            for i in graph[curr_node]:
                v, weight = i[0], i[1]
                alt = dist[curr_node] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(p_queue, (dist[v], v))
        
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = dd(list)
        for i in times:
            graph[i[0]].append((i[1], i[2]))
        
        nodes = (N + 1)
        dist = [sys.maxsize] * nodes
        self.dijsktra_dist(K, dist, graph)
        dist.pop(0)
        for i in dist:
            if i == sys.maxsize:
                return -1
            
        return max(dist)
