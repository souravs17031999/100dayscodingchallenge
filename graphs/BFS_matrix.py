# BFS traversal for matrix representation of graph
from collections import deque

def BFS(matrix, source):

    queue = deque([])
    visited = set()

    queue.append(source)
    visited.add(source)

    while queue:
        curr = queue.popleft()
        print(curr, end = " ")

        for j in range(len(matrix)):
            if matrix[curr][j] and j not in visited:
                queue.append(j)
                visited.add(j)


import random
if __name__ == '__main__':
    N = 4
    # matrix = [[random.randint(0, 1)] * N for _ in range(N)]
    matrix = [[0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 0, 0, 1]]

    print(matrix)
    BFS(matrix, 1)
