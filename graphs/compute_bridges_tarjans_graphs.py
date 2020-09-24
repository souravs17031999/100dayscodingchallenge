# Program for printing the bridges in the undirected graph
# Bridges are single point of failure such that if we remove that edge, the graph becomes disconnected 
# The observation is that if we remove one bridge (edge), then number of connected compoenents should 
# increase which is due to graph becomming disconnected. So, we simply keep removing edge one by one, 
# check if number of connected components increase, then again add that edge back into the graph.
# This will take 0(E * (E + V)), E is edges, V is vertices.

# Can we do better ?
# Yes, we can observe that edge (u, v) can be bridge if there is no back edge from v to u or any of the 
# ancestors of u.
# Because if there would be back edge, then removing it will not affect anything as it can be reached via 
# some another vertex using that back edge, thus it is not single point of failure anymore.

# We will use two arrays disc[] and low[], disc is first discovery time initilazed to zero, low for every 
# vertex v, the discovery time of the earliest discovered vertex to which v or any of the vertices in the 
# subtree rooted at v is having a back edge.

# disc[] doesn't changes since, its the first time discovery while doing our DFS traversal, but low[] will 
# be updated because initially in low[], node doesn't know about future if there is any back edge or not
# then after backtracking, we will update the low considering both cases, if there is any back edge or not.

# Time will be immproved to 0(E + V) due to single DFS traversal.

# -------------------------------------------------------------------------------------------------------

# First method : 

from collections import defaultdict as dd 

def remove_edge(graph, u, v):
    idx = graph[u].index(v)
    del graph[u][idx]
    idx = graph[v].index(u)
    del graph[v][idx]
    
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)  

def dfs(graph, source, visited):
    visited.add(source)
    for i in graph[source]:
        if i not in visited:
            dfs(graph, i, visited)
    
def count_components(graph, nodes):
    
    visited = set()
    count = 0
    for i in range(nodes):
        if i not in visited:
            count += 1
            dfs(graph, i, visited)
    return count 

def compute_bridges(roads):
    
    graph = dd(list)
    
    for i in roads:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    nodes = len(graph)
    ori_conn = count_components(graph, nodes)
    bridge = 0
    print(graph)
    res = []
    for i in roads:
        remove_edge(graph, i[0], i[1])
        final_conn = count_components(graph, len(graph))
        if final_conn > ori_conn:
            res.append(i)
        add_edge(graph, i[0], i[1])    
    
    print(res)
        

        
# second method :


def dfs(u, visited, parent, low, disc, graph, res):
    
        visited[u]= True

        disc[u] = dfs.timer
        low[u] = dfs.timer
        dfs.timer += 1 # static variable

        for v in graph[u]: 
            
            if not visited[v] : 
                parent[v] = u 
                dfs(v, visited, parent, low, disc, graph, res) 

                low[u] = min(low[u], low[v]) 


                if low[v] > disc[u]: 
                    res.append([u, v])


            elif v != parent[u]: 
                low[u] = min(low[u], disc[v]) 


def compute_bridges(roads):
    
    graph = dd(list)
    
    for i in roads:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    nodes = len(graph)
    visited = [False] * nodes 
    disc = [float('inf')] * nodes 
    low = [float('inf')] * nodes 
    parent = [-1] * nodes 
    dfs.timer = 0
    res = []
    for i in range(nodes):
        if not visited[i]:
            dfs(i, visited, parent, low, disc, graph, res)
    
    print(res)
            
    
# main driver function 
if __name__ == '__main__':
    graph = dd(list)
    roads = [[0, 1], [1, 2], [2, 3]]  # given input showing connections between nodes 
    compute_bridges(roads)
