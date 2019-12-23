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
    def __init__(self):
        self.dd = dd(list)

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
            visited = [False] * len(self.dd)
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
            print("No source vertex !")


if __name__ == '__main__':
    # input_list = list(map(int, stdin.readline().strip().split()))
    print('adjlist representation: ')
    g = adjgraph()
    g.addEdge(0, 2)
    g.addEdge(0, 1)
    g.addEdge(2, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printGraph()
    g.BFS(2)
