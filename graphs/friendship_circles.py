# Program for computing number of friend circles represented as adjacency list or matrix.
# Follow up - Secondly, we also want to return list of all friends in each friend circle.
# 
# A classroom consists of N students, whose friendships can be represented in an adjacency list. 
# For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.
#
# {0: [1, 2],
# 1: [0, 5],
# 2: [0],
# 3: [6],
# 4: [],
# 5: [1],
# 6: [3]} 
#
# Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, 
# this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.
# 
# Friendship circles can be represented using a graph of social circles like one below and it is undirected graph : 
#
#
#                
#
#                    {0} ----- {1} ----- {5}
#                     |
#                    {2}
#
#                    {3} --------- {6}
#                      
#                    {4}
#
# From the above graph, it can be very well seen that total friend circles are actually the total connected components in the graph = 3.
# -----------------------------------------------------------------------------------------------------------------------------------------
# If represented using adjacency list , then directly use it or if represented using matrix, then convert it into adj list first.

from collections import defaultdict as dd, deque

def dfs(source, graph, visited):
    visited.add(source)
    for i in graph[source]:
        if i not in visited:
            dfs(i, graph, visited)

def compute_friends(graph, V):
    
    visited = set()
    count = 0
    for i in range(V):
        if i not in visited:
            dfs(i, graph, visited)
            count += 1
    
    print(f"friends circles : {count}")

# So, if now we want to return the list of all friends in each friendship circle, then we need to make a minor change so that in each dfs call, all friends are appended 
# to a friendship list and then overall appended to final list.
# EX. for the above input, output should look like : [[0, 1, 5, 2], [3, 6], [4]]


from collections import defaultdict as dd, deque

def dfs(source, graph, visited, temp):
    visited.add(source)
    temp.append(source)
    for i in graph[source]:
        if i not in visited:
            dfs(i, graph, visited, temp)

def compute_friends(graph, V):
    
    visited = set()
    count = 0
    output = []
    for i in range(V):
        temp = []
        if i not in visited:
            dfs(i, graph, visited, temp)
            count += 1
            output.append(temp)
    
    print(f"friends circles : {count}")
    print(output)
    
if __name__ == '__main__':
    graph = dd(list)
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(0)
    graph[1].append(5)
    graph[2].append(0)
    graph[3].append(6)
    graph[4]
    graph[5].append(1)
    graph[6].append(3)
    
    V = len(graph)
    print(graph)
    print(V)
    compute_friends(graph, V)
