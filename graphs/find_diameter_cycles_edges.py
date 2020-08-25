# Program to find the diameter, cycles and edges of a Wheel Graph
# Wheel Graph: A Wheel graph is a graph formed by connecting a single universal vertex to all vertices of a cycle. Properties:-

# Wheel graphs are Planar graphs.
# There is always a Hamiltonian cycle in the Wheel graph.
# Chromatic Number is 3 and 4, if n is odd and even respectively.

# Problem Statement: Given the Number of Vertices in a Wheel Graph. The task is to find:
#
# The Number of Cycles in the Wheel Graph.
# Number of edges in Wheel Graph.
# The diameter of a Wheel Graph.
Number of Cycle = (vertices * vertices) - (3 * vertices) + 3
Number of edge = 2 * (vertices - 1)
Diameter = if vertices = 4, Diameter = 1
           if vertices > 4, Diameter = 2
