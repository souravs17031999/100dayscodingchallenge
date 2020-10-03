# Program to print the euler path in the given graph.
# print the eulerian trail.
# STEPS : 
# * Make sure the graph has either 0 or 2 odd vertices.
# * If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.
# * Follow edges one at a time. If you have a choice between a bridge and a non-bridge, always choose the non-bridge.
# * Stop when you run out of edges.
#
# This is called Fleury algorithm.
# ----------------------------------------------------------------------------------------------------------------------------------
# TIME : 0((E + V) * (E + V)) == O(E ^ 2)
# Time complexity can be improved to 
# 0(E)  in linear time using Hierholzer’s algorithm.
# Below is optimized algorithm in linear time : 

from collections import defaultdict as dd, deque 
    
def print_euler_circuit(graph):
    
    if len(graph) == 0:
        return []
    
    source = 0
    curr_path = deque()
    curr_path.append(source)
    circuit = []
    
    while curr_path:
        
        curr = curr_path[-1]
        
        if graph[curr]:
            
            curr_path.append(graph[curr].pop())
        
        else:
            circuit.append(curr_path.pop())
    
    print(circuit[::-1])
        
    
if __name__ == '__main__':
    
    graph = dd(list)
    graph[0].append(1)
    graph[1].append(3)
    graph[1].append(2)
    graph[2].append(0)
    graph[3].append(4)
    graph[4].append(1)
    
    print_euler_circuit(graph)
