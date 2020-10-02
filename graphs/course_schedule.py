# Program for computing ordering for scheduling the given number of courses.
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
#
# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# We can actually solve this problem using graph representation of the courses schedule list, as we need the ordering condition [u, v], where u comes before v.
# So, infact in the list of courses above it is given reverse, so we will contruct the graph using reverse ordering as in if [1, 0] is given, then we will make graph as 
# [0] => [1] due to the conditions given in the question.
# And we will apply topological sorting, also it is not guranteed that it will not contain a cycle, hence we here use kahn's algo which can also detect if cycle is present.
# TIME : 0(E + V)

from collections import deque, defaultdict as dd
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = dd(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
            
        in_degree = [0] * numCourses
        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1
        
        count = 0
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for i in graph[curr]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            count += 1
        
        if count != numCourses:
            return []
        else:
            return res
        
