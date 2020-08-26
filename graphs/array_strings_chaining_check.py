# Given an array of strings, find if the given strings can be chained to form a circle. A string X can be put before another string Y in circle
# if the last character of X is same as first character of Y.
# Input: arr[] = {"for", "geek", "rig", "kaf"}
# Output: Yes, the given strings can be chained.
# The strings can be chained as "for", "rig", "geek"
# and "kaf"
# Input: arr[] = {"aaa", "bbb", "baa", "aab"};
# Output: Yes, the given strings can be chained.
# The strings can be chained as "aaa", "aab", "bbb"
# and "baa"
# Input : arr[] = [“ijk”, “kji”, “abc”, “cba”]
# Output : No
# The idea is to create a directed graph of all characters and then find if their is an eulerian circuit in the graph or not.
# If there is an eulerian circuit, then chain can be formed, otherwise not.
# Note that a directed graph has eulerian circuit only if in degree and out degree of every vertex is same, and all non-zero degree
# vertices form a single strongly connected component.


from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

if __name__ == '__main__':

    # creating a graph for nodes made up of first and last char for every string.
    arr1 = ["for", "geek", "rig", "kaf"]
    graph = Graph(26)
    for i in range(len(arr1)):
        graph.add_Edge(ord(arr1[i][0]) - ord('a'), ord(arr1[i][len(arr1[i])-1]) - ord('a'))

    graph.printGraph()

    # After this, we simply need to check if graph is singly strongly connected graph that means each vertex should be reachable using any vertex.
    # also, for every vertex, indegree and outdegree should be same.
