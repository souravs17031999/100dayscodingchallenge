# Program for checking the cycle in the graph with degree of nodes in the graph and print the nodes in the cycle.
# EX .
#                1 ----- 0 ------ 3
#                |   /            |
#                2                4
#
# So, here, we have one cycle containing [0, 1, 2]
# ------------------------------------------------------------------------------------------------------------------
# Actually we already know we can detect cycle in the graph using simple DFS but know we also want to know which exact nodes
# are in the cycle.
# So, intuition is about degree of nodes in the graph, since all the nodes contained in the cycle will be having atleast 2 degree as they in the cycle
# and to complete the cycle they can never have less than 2 degree.
# It means all the nodes having degree 1 will be useless for us and all the nodes having degree 2 or more, are useful for us as they contains cycle.
# So, we one by one remove the nodes from the graph starting from whose in-degree is 1, and similarly for its adjacent nodes.
# In this way we also maintain a queue, which can help us to search in the above way BFS type traversal.
# if finally, there are any nodes which are not visited after the traversal, they are the nodes in cycle.
# -------------------------------------------------------------------------------------------------------------------

from collections import defaultdict as dd, deque
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

    def detect_cycle_degree(self):

        in_degree = {}
        for i in self.graph:
            in_degree[i] = len(self.graph[i])

        visited = set()
        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 1:
                queue.append(i)

        while queue:

            curr = queue.popleft()

            visited.add(curr)
            for i in self.graph[curr]:
                in_degree[i] -= 1

            for i in range(len(in_degree)):
                if in_degree[i] == 1 and i not in visited:
                    queue.append(i)

        res = []
        for i in self.graph:
            if i not in visited:
                res.append(i)

        if res:
            print(res)
        else:
            print("CYCLE NOT DETECTED !")



# driver test function
if __name__ == '__main__':

    graph = Graph(5)
    graph.add_Edge(0, 4)
    graph.add_Edge(0, 1)
    graph.add_Edge(0, 3)
    graph.add_Edge(1, 2)
    graph.add_Edge(3, 4)
    graph.add_Edge(3, 1)
    graph.detect_cycle_degree()
