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
#
#  ---{0}
# |    |
# |   {1}
#  /    \
# {3}   {2}
# 
# Here, if we remove {1-3}, then also graph will not be affected, because there is a back edge from {3-0}, and so {1-3} can't be bridge, and similar with {0-3}. 
# But if we remove {1-2}, then we can't reach node with value "2", hence {1-2} is a critical edge/bridge in the graph.
#
# We will use two arrays disc[] and low[], disc is first discovery time initilazed to zero, low for every 
# vertex v, the discovery time of the earliest discovered vertex to which v or any of the vertices in the 
# subtree rooted at v is having a back edge.

# disc[] doesn't changes since, its the first time discovery while doing our DFS traversal, but low[] will 
# be updated because initially in low[], node doesn't know about future if there is any back edge or not
# then after backtracking, we will update the low considering both cases, if there is any back edge or not.
#
# Sample dry run of the intuition : 
#    
#     {0} --------- {1}                   CUrrently, dfs traversal starting from 0, we have reached till 2, 
#      |  \           |                   => disc:   [0, 1, 2, -1, -1]
#     {3}   \         |                   => low:    [0, 1, 2, -1, -1]
#      |       \      |                   => parent: [-1, 0, 1, -1, -1] 
#     {4}          \  |                   => indices [ 0, 1, 2, 3,  4] 
#                    {2}
#
#
# Now, in dfs traversal starting from {2}, we reached {0} again which is also visited and it is not parent of {2}, that's why it indicates a  back edge, and hence, 
# low will now be updated to min(low(0), low(2)) => low[2] = 0 because at t=0, as soon we start traversal from {0}, this node {2} will be discovered in the same time frame.
# Now, this also indicates there is no bridge between 1-2 due to back edge present in the ancestors of them.
# Then, we backtrack from {2}, and reach {1}, so, now we finished dfs traversal of {1}, hence its time to update low of {1}, because now we know that there is a back edge 
# which was earlier not known to us, and hence we use updated value of low[2] to update our low value of low[1] = min(low[1], low[2]) => low[1] = 0.
# Now, since low[1] < disc[2], so no this is not bridge (which also is true due to back edge present).
# -------------------------------------------------------------------------------------------------------------------------------
#
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
                
                # after finishing traversal, we update low value and since if there would be back edge present, this would become lesser than previous.
                low[u] = min(low[u], low[v]) 

                # if there would be any back edge, then low would have to become lesser but if it greater then it indicates bridge.
                if low[v] > disc[u]: 
                    res.append([u, v])

            # now, if it is already visited but is not a parent of node, then this means there is a back edge and which updates low value.
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
