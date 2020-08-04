# program to implement graph TRAVERSAL - breadth first search and depth first search
from sys import stdin, stdout
from collections import defaultdict as dd
import collections

# Note : use below code if want to use adj matrix , otherwise adjlist is more useful here
# class adjmatrix:
#     def __init__(self, V):
#         self.vertices = V
#         self.mat = [[0]*self.vertices for _ in range(self.vertices)]
#
#     def addEdge(self, u, v):
#         self.mat[u][v] = 1
#         self.mat[v][u] = 1
#
#     def printGraph(self):
#         m = len(self.mat)
#         n = len(self.mat[0])
#         for i in range(m):
#             for j in range(n):
#                 print(f"{self.mat[i][j]}", end = " ")
#             print()

# class for construcing adjacency lists for a graph
class adjgraph:
    # intiliazing the graph with defaultdict list parameter and size which is maximum no of nodes
    def __init__(self, size):
        self.dd = dd(list)
        self.V = size

    # adding a edge means appending to a list maintained which are the values of key which is the source node
    def addEdge(self, u, v):
        self.dd[u].append(v)
        # use below if using undirected graphs
        #self.dd[v].append(u)

    # displaying the entire adjacency list
    def printGraph(self):
        for i in self.dd:
            print(f"{i}: ", end = "")
            for j in self.dd[i]:
                print(f"{j}", end = ", ")
            print()

    # traversing graphs in BFS way which says first discovered nodes will be explored first, that means it goes with FIFO principle, that means we need to use queue in order to traverse it
    def BFS(self, s):
        if s in self.dd:
            print("BFS TRAVERSAL : ", end = "")
            visited = [False] * self.V
            queue = collections.deque([])
            queue.appendleft(s)
            visited[s] = True
            while queue:
                p = queue.pop()
                print(p, end = "-")
                for i in self.dd[p]:
                    if visited[i] == False:
                        queue.appendleft(i)
                        visited[i] = True

        else:
            print("Source vertex doesn\'t exist !")

    # traversing the DFS way which says go on from a source node till it can no longer move on and then backtrack from there and search for another path , therefore we need the currently inserted value (enqueued), thus we need to have stack which can help in this as we need to see and check the last one so LIFO.
    # below graph doesn't takes source vertex as parameters but rather another function "DFS" calls this below one repeatedly for every other vertex so that disconnected vertices also get traversed.
    def DFSUtil(self, s, visited):
        stack = []
        stack.append(s)
        while stack:
            p = stack.pop()
            if p not in visited:
                print(p, end = "-")
                visited.add(p)

            for i in self.dd[p]:
                if visited.add(p):
                    stack.append(i)

    # main DFS function which runs DFS for every vertex, thus ensuring every disconnected vertex also gets traversed
    def DFS(self):
        visited = set()
        print("DFS TRAVERSAL : ", end = "")
        for i in range(self.V):
            if i not in visited:
                self.DFSUtil(i, visited)

# main function
if __name__ == '__main__':
    # input_list = list(map(int, stdin.readline().strip().split()))
    print('adjlist representation: ')
    # mark the no of vertices properly
    # also remember that this assumes indexing of 0 based on array , so if the vertices starts from 1, then we have to replace every i by i - 1 whenever indexing in the above code
    # Note : whenever , graph values are like more than no of nodes ex. size = 4, values = 10, 20, 30...100.. it will throw error because there exists no index in the visited for these values, hence we need to use dictionery hashing for implementing this condition.
    # visited = {} for i in self.dd: visited[i] = False , it will ensure that only those vertices are included in dictionery for which some value exists , and no longer depends on maximum no of nodes.
    g = adjgraph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printGraph()
    g.BFS(2)
    print()
    g.DFS()
