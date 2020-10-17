# Program for constructing the entire itinerary from the given nested list of tickets given in the form [from, to].
#  All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#             But it is larger in lexical order.
#
# ------------------------------------------------------------------------------------------------------------------------------------
# Firstly, we can think of starting always from 'JFK', and then searching 'JFK' from complete list and construct temp list containing of all "to's", 
# and then sorting it so that lexically sorting will be there.
# This can take up to 0(N * N log(N)).
# Can we do more better by representing it some other way ?
# We can actually think of it as graph based adjacency list representation which consists of key as from (which will be unique codes) and all "to's", destination will be 
# appended to that key as values in a list.
# We will use defaultdict for this.
# Also, we will now sort all the individual graph keys so that we always choose lexical smaller first.
# Now, while traversing DFS ways, we will use iterative DFS using stack so that if any key has nothing to travel, dead end, then also we can pop from top of stack, add it to  
# to our result list , come back and start traversing the next node in the defaultdict (graph).
# Final, result list would be in reverse order, so, we reverse it befoe returning from the function.
# --------------------------------------------------------------------------------------------------------------------------------------


from collections import defaultdict as dd, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = dd(list)
        stack = deque()
        output = []
        
        for i in tickets:
            graph[i[0]].append(i[1])
        
        for i in graph:
            graph[i].sort()
        
        
        stack.append('JFK')
        
        while stack:
            
            curr = stack[-1]
            
            if not graph[curr]:
                output.append(curr)
                stack.pop()
            else:
                stack.append(graph[curr][0])
                del graph[curr][0]
        
        output.reverse()
        return output
                
