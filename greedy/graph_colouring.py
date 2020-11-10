# Problem : Given a graph, we need to color all the vertices such that no two adjacent vertices
# should be coloured same.
# ------------------------------------------------------------------------------------
# NOTE : Firstly, we need to convince ourselves that given a graph whose max degree of any node = "D", can be coloured properly with ATMOST = "D+1" COLORS.
# Brute force way of colouring would be to check for all possible orderings of all colors, like say we have graph with maximum degree of D = 3, and then it would be coloured
# with atmost 4 colors, now if we start checking for all combinations : 
# Total : 4^12 , in general : 0(D^N) combinations and that would be exponential.
# ------------------------------------------------------------------------------------
# Colouring the graph is NP-HArd problem where there is no efficient optimal solution
# but there is a quick algorithm that halts and gives a good approximate in number of situations.
# So, we apply here greedy approach to colour the first vertex and second which ever is avaiable
# at that moment of time, and then same carrying on for all the vertices in the graph.
# NOTE : ordering of the vertices can determine the solution found.
# ------------------------------------------------------------------------------------
# So, we can maintain boolean array saying which color is avaiable and which not,
# and for that we can look up all the adjacent elements and mark those as unavaiable.
# Then, we can loop around the boolean array and simply, assign the first avaiable index color
# and similarly for the remaining vertices.
# The greedy part is that we are assinging whichever color is presently avaiable and don't
# think about the future or reconsider our past decision.
# TIME : 0(D * N), D IS MAX DEGREE, N IS TOTAL NODES.
# -------------------------------------------------------------------------------------
# Can we do better ?
# We can reduce this to linear time in 0(E + V).

from collections import defaultdict as dd
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for i in range(self.V):
            print(i, end = "->")
            for j in self.graph[i]:
                print(j, end = " ")
            print()

    def color_graph(self):

        result = [None] * self.V
        available = [True] * self.V

        result[0] = 0

        for i in range(1, self.V):
            print(result)
            for j in self.graph[i]:
                if result[j] != None:
                    available[result[j]] = False

            for color in range(self.V):
                if available[color]:
                    break

            result[i] = color

            for j in self.graph[i]:
                if result[j] != None:
                    available[result[j]] = True

        print(result)
if __name__ == '__main__':

    graph = Graph(5)
    graph.add_Edge(0, 1)
    graph.add_Edge(0, 2)
    graph.add_Edge(1, 3)
    graph.add_Edge(2, 3)
    graph.add_Edge(3, 4)
    graph.printGraph()
    graph.color_graph()
