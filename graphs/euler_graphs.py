# Program to check and verify euler graph/ circuit and euler path for the given graph.
# Euler graph/circuit : 
# * All vertices with non-zero degree are connected. We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path.
# * All vertices have even degree.
# Euler path : 
# * Same as condition (a) for Eulerian Cycle.
# * If zero or two vertices have odd degree and all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph.
# NOTE : a graph with no edges is considered Eulerian because there are no edges to traverse.
# --------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(E + V)

from collections import defaultdict as dd, deque 


def check_connectivity(nodes, visited, graph):
    
    for i in range(nodes):
        if not visited[i] and in_degree[i]:
            return True
    
    return False

def count_odd_degree(in_degree, graph):

    for i in in_degree:
        if i & 1:
            return True
    
    return False
    

def dfs(source, visited, graph):
    
    visited[source] = True
    for i in graph[source]:
        if not visited[i]:
            dfs(i, visited, graph)

def check_euler_circuit(graph):
    
    nodes = len(graph)
    visited = [False] * nodes
    in_degree = [0] * nodes
    for i in graph:
        for j in graph[i]:
            in_degree[i] += 1
    
    source = None
    for i in range(nodes):
        if graph[i]:
            source = i
            break
    
    if source == None:
        print("Euler Graph !")
        return
    
    dfs(source, visited, graph)
    print(visited) 
    if check_connectivity(nodes, visited, graph):
        print("Not a Euler graph !")
        return
    
    if count_odd_degree(in_degree, graph):
        print("Not a Euler graph !")
        return
    
    print("Euler graph exists!")
    

def check_euler_path(graph):
    
    nodes = len(graph)
    visited = [False] * nodes
    source = None
    for i in range(nodes):
        if graph[i]:
            source = i
            break
    
    if source == None:
        print("Euler Graph exists!")
        return
    
    dfs(source, visited, graph)
    for i in range(nodes):
        if not visited[i]:
            print("Not euler path")
            return
    
    print("Euler path exists!")
    
    
if __name__ == '__main__':
    graph = dd(list)
    graph[0].append(1)
    graph[0].append(2)
    graph[0].append(3)
    graph[0].append(4)
    graph[1].append(0)
    graph[1].append(2)
    graph[2].append(1)
    graph[2].append(0)
    graph[3].append(0)
    graph[3].append(4)
    graph[4].append(0)
    graph[4].append(3)
    
    check_euler_circuit(graph)
    check_euler_path(graph)
