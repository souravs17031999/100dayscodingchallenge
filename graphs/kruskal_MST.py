# Program to compute MST using kruskal's algo.
# We have already seen Prim's algo which works faster for dense graphs.
# For sparse graphs, kruskals's algo is faster.
# TIME : O(E log E) + O(E log V)
# Steps : 
# - Sort all the edges in increasing order of weight.
# - Repeat : 
#   - Pick the smallest edge
#   - Check if the new edge forms a cycle in our spanning tree being formed 
#   - If cycle is not formed, include the edge, otherwise discard the edge.
# - Repeat above till V-1 edges are all included in MSTset.
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#       {1} ---- {4} 
#     /    \   /     \ {5}
#   {0}     /  \      /
#      \ {2} ---- {3}
#         
#
# Sorted edge list : 
#
#  SRC DST WT
#   0  1   1
#   1  3   1    
#   2  4   1
#   0  2   2
#   2  3   2
#   3  4   2
#   1  2   3
#   1  4   3
#   4  5   3
#   3  5   4 
# Now one by one include edges, which do not form the cycle.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

pseduo code: 

sort(adj_list)
i, j = 0,0
MST = []
while i < V - 1 and j < E:
  fromP = find(adj_list[j].src)
  toP = find(adj_list[j].dst)
  if fromP == toP:
    j ++
     continue
  union(fromP, toP)
  MST.append(adj_list[j])
  i ++ 
  
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
