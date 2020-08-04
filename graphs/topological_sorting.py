# Program to do topological sorting
# Two algorithms are considered....
# Firstly, it's a slight modification of DFS as in DFS here also we need to go in one direction but also
# we need to maintain a condition that for any given (u -- > v), we need that u should be coming before V.
# This is highly useful in package dependency graphs, scheduling algorithms etc.
# So, we need a extra stack to maintain this ordering and push the current node on the stack,
# only when all of its adjacent vertices are finished exploring, and then after going through all the
# nodes, we can simply pop off the stack elements and pring them.
# NOTE : topological SORTING / ORDERING IS ONLY POSSIBLE FOR DAG (DIRECTED ACYCLIC GRAPH)
# IF THERE IS ANY CYCLE, THEN WE WILL NOT BE ABLE TO PERFORM topological ORDERING.
# BELOW DFS APPROACH WILL NOT BE ABLE TO DETECT IF THERE IS ANY CYCLE OR NOT, AND WILL RESULT
# IN SOME ORDERING ANYHOW.
# ----------------------------------------------------------
#
#       3     1
#          \>/>
#           0
#         />\>
#       4   2
# -----------------------------------------------------------
# Now, if we run normal DFS from 0, then we will get : 0, 1, 2, 3, 4
# But we need : 3, 4, 0, 1, 2 or 4, 3, 0, 1, 2 or 4, 3, 0, 2, 1 or 3, 4, 0, 1, 2
# So, the logic is to keep a stack and push the current element onto stack, only when we explored
# all the adjacent vertices of the current node, this ensures that when we pop from stack, we get
# complete the contrainst that for any (u, v) u comes before v.
# ------------------------------------------------------------
# Use of extra stack :
# TIME : 0(E + V)


from collections import defaultdict as dd, deque
class Graph:

    def __init__(self, size):
        self.V = size
        self.graph = dd(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in range(self.V):
            print(i, end = " -> ")
            for j in self.graph[i]:
                print(j, end = ", ")
            print()

    # ---------------------------------------------------
    # DFS APPROACH WITH EXTRA STACK
    def DFS(self, v, visited, stack):

        visited.add(v)

        for i in self.graph[v]:
            if i not in visited:
                self.DFS(i, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = set()
        stack = deque([])
        rec_stack = deque([])
        for i in range(self.V):
            if i not in visited:
                self.DFS(i, visited, rec_stack)


        while rec_stack:
            print(rec_stack.pop(), end = " ")

    # ---------------------------------------------------
    # Kahn's algorithm using in-degree and out -degree
    # A DAG G has at least one vertex with in-degree 0 and one vertex with out-degree 0.
    # TIME : 0(E + V)
    # ---------------------------------------------------
    # This algorithm steps :
    # * Compute in degree of all the vertices and enqueue into a new queue , all the 0 in degree vertices
    # * while queue is not empty, again enqueue curr node into queue if neighbouring nodes have 0 in degrees
    # * keep track of all the count of visited nodes, if after the queue is empty, if count of visited nodes
    # is not equal to total nodes, then NO POSSIBLE ordering is required, since it contained the cycle.
    # TIME : 0(E + V), SPACE : 0(V)
    # THIS IS A GOOD algorithm, AS IT CAN ALSO DETECT CYCLE.

    def topological_BFS(self):

        in_degree = [0] * self.V

        # computing in_degree for all vertices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = deque([])
        # push all 0-indegree vertices initially to queue
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0
        top_order = []

        while queue:
            curr = queue.popleft()
            top_order.append(curr)

            for i in self.graph[curr]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            count += 1

        if count != self.V:
            print("NO ORDERING, CYCLE DETECTED !")
        else:
            print(top_order)


# driver test function
if __name__ == '__main__':

    g= Graph(6)
    g.add_Edge(5, 2);
    g.add_Edge(5, 0);
    g.add_Edge(4, 0);
    g.add_Edge(4, 1);
    g.add_Edge(2, 3);
    g.add_Edge(3, 1);
    g.topological_sort()
