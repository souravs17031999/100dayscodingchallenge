# DFS traversal for MAZE representation of graph
# here, we use matrix representation

from collections import deque

def DFSUtil(matrix, source, visited, goal):

    visited.add(source)
    if source == goal:
        print("GOAL NODE REACHED !")
        return

    for j in range(len(matrix)):
        if matrix[source][j] and j not in visited:
            DFSUtil(matrix, j, visited, goal)

def DFS(matrix, start, goal):
    visited = set()
    DFSUtil(matrix, start, visited, goal)

def pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = " ")
        print()

import random
if __name__ == '__main__':
    N = 6
    # matrix = [[random.randint(0, 1) for _ in range(N)] for _ in range(N)]
    matrix = [[1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1]]
    pretty_print(matrix)
    DFS(matrix, 2, 2)
