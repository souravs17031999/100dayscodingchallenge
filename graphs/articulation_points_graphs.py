# Program to find all the articulation points in the given undirected graph.
# Now, articulation points are single point of failure for the network which when removed increases the number of connected components and graph becomes 
# disconnected.
# So, basically, after removing a node, if the graph remains connected, that is no. of connected compoenents/ subgraphs doesn't increases, then it's not a articulation point.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Now, let's think about what are subgraphs and how will they help us finding our goal.
#
#
#    {0}  c = 2    > this means if we remove {0}, then there will be two subgraphs, no of connected comp. will increase from 1 -> 2.
#   /  \
#  {1}  {2}
#
#    {0}     c = 1 > this means there is only one subgraph/conn. component, no of connected comp. will remain same and equal to 1.
#   /  \
#  {1} - {2}
#
#
#   {0}   c = 3 > this means there is three subgraphs and conn. comp increased from 1 to 3, if we remove {0}.
#   / | \
# {1} {2} {3}
#
# In all the above cases, we tried to find the children count (c) / connected compo / subgraphs after removing {0} and we can see in I and III case, it increased but not in II.
# That also means, {0} is an articulation point in I and III but not in II.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Brute force approach will be same which was for finding bridges in the graph but here it's for nodes (articulation point).
# So, for each node in the graph, 
# We delete it from the graph, and then calculate conn. comp.
# If that increased from those which was before removal, then it means this point is an articulation point.
# TIME : 0(V * (E + V))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Can we do better than this ?
# Case I : If node U is a root of the DFS tree, and it has atleast two children then traversing DFS for each outgoing edge from root, 
# increment the chidlren counter which if at final is > 1, then it means it is a articulation point. (Examples are same as shown above).
# Case II : if node u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.
# 
#
#
#       ----{0}
#       |    |
#       |    {1}
#       |   / | \  
#       {2}-{3} {4}
#
# Here, we see node {1}, and if we remove this node then also subgraphs remains constant, as there is also back edge from {2-0} which are ancestors of them.
# Hence, {1} can't be articulation point with respect to subgraph {2-3} but can it be never ? 
# If we see from respect to second subgraph containing only {4}, then remvoing {1}, will increase the conn. compo, hence it can be articulation point for this case.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Concept of disc[] and low[] will be used here (for case II) and will be similar to finding bridges algorithm.
# 
# Sample dry run for the intuition : 
#
#   {0} ----- {1} 
#    |\        |
#    |   \     |             => starting DFS traversal from {0}, after fininshing all the traversal : 
#    |     \   |             => disc :   [0, 1, 2, 3, 4, 5]         
#    |       \ {2}           => low :    [0, 0, 0, 3, 4, 5]
#   {3}                      => parent:  [-1, 0, 1, 0, 3, 3]
#  /  \                      => AP :     [T, F, F, T, F, F]
# {4}  {5}
#
# Shows, {0} and {3} are two articulation points for the graph.
# 
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TIME : 0(E + V) due to single traversal of the entire graph.


