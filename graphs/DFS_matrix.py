# DFS traversal for matrix representation of graph

from collections import deque

def DFSUtil(matrix, source, visited):

    visited.add(source)
    print(source, end = " ")

    for j in range(len(matrix)):
        if matrix[source][j] and j not in visited:
            DFSUtil(matrix, j, visited)

def DFS(matrix, start):
    visited = set()
    DFSUtil(matrix, start, visited)

import random
if __name__ == '__main__':
    N = 4
    # matrix = [[random.randint(0, 1)] * N for _ in range(N)]
    matrix = [[0, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1]]

    print(matrix)
    DFS(matrix, 2)
