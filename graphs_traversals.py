# program to implement graph TRAVERSAL - breadth first search and depth first search
from sys import stdin, stdout
from collections import defaultdict as dd
import collections
class adjmatrix:
    def __init__(self, V):
        self.vertices = V
        self.mat = [[0]*self.vertices for _ in range(self.vertices)]

    def addEdge(self, u, v):
        self.mat[u][v] = 1
        self.mat[v][u] = 1

    def printGraph(self):
        m = len(self.mat)
        n = len(self.mat[0])
        for i in range(m):
            for j in range(n):
                print(f"{self.mat[i][j]}", end = " ")
            print()

class adjgraph:
    def __init__(self, size):
        self.dd = dd(list)
        self.V = size

    def addEdge(self, u, v):
        self.dd[u].append(v)
        #self.dd[v].append(u)

    def printGraph(self):
        for i in self.dd:
            print(f"{i}: ", end = "")
            for j in self.dd[i]:
                print(f"{j}", end = ", ")
            print()
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

    def DFSUtil(self, s, visited):
        stack = []
        stack.append(s)
        while stack:
            p = stack.pop()
            if visited[p] == False:
                print(p, end = "-")
                visited[p] = True

            for i in self.dd[p]:
                if visited[i] == False:
                    stack.append(i)

    def DFS(self):
        visited = [False] * self.V
        print("DFS TRAVERSAL : ", end = "")
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
if __name__ == '__main__':
    # input_list = list(map(int, stdin.readline().strip().split()))
    print('adjlist representation: ')
    # mark the no of vertices properly
    # also remember that this assumes indexing of 0 based on array , so if the vertices starts from 1, then we have to replace every i by i - 1 whenever indexing in the above code
    # Note : whenever , graph values are like more than no of nodes ex. size = 4, values = 10, 20, 30...100.. it will throw error because there exists no index in the visited for these values, hence we need to use set hashing for implementing this condition.
    # visited = {} for i in self.dd: visited[i] = False
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
