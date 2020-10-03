# Program for Bi-directional BFS 
# Logic is to start from source vertex and also simulataneously start traversal from target node also and we will check if at any time, there is intersecting node.
# And if we calculate distance from both intermediate nodes from start and target, dist = L1 + L2 - 1.
# Overall time complexity will be same 0(E + V), but space is optimized.
# ---------------------------------------------------------------------------------------------------------------------
from collections import defaultdict as dd, deque 

def is_intersect(nodes, s_visited, t_visited):
    
    for i in range(nodes):
        if s_visited[i] and t_visited[i]:
            return i
    
    return -1

def BFS(queue, visited, graph):
    
    curr = queue.popleft()
    for i in graph[curr]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

def add_Edge(graph, u, v):

    graph[u].append(v)
    graph[v].append(u)

def bi_BFS(nodes, graph):
    
    s, t = 0, 14
    nodes = nodes 
    s_visited = [False] * (nodes + 1)
    t_visited = [False] * (nodes + 1)
    
    intersect_node = -1
    s_queue = deque()
    t_queue = deque()
    
    s_queue.append(s)
    t_queue.append(t)
    s_visited[s] = True
    t_visited[t] = True
    
    while s_queue and t_queue:
        
        BFS(s_queue, s_visited, graph)
        BFS(t_queue, t_visited, graph)
        
        intersect_node = is_intersect(nodes, s_visited, t_visited)
        
        if intersect_node != -1:
            print(f"Path exist between {s} and {t} and intersection at {intersect_node}")
            return
        
    print("Path doesn't exist !")
    

if __name__ == '__main__':
    
    graph = dd(list)
    add_Edge(graph, 0, 4)
    add_Edge(graph, 1, 4)
    add_Edge(graph, 2, 5)
    add_Edge(graph, 3, 5)
    add_Edge(graph, 4, 6)
    add_Edge(graph, 5, 6)
    add_Edge(graph, 6, 7)
    add_Edge(graph, 7, 8)
    add_Edge(graph, 8, 9)
    add_Edge(graph, 8, 10)
    add_Edge(graph, 9, 11)
    add_Edge(graph, 9, 12)
    add_Edge(graph, 10, 13)
    add_Edge(graph, 10, 14)
    bi_BFS(15, graph)
