# Program for computing all the shortest distances for the nearest 0 for every cell in the matrix.
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
# Example 2:
#
# Input:
# [[0,0,0],
# [0,1,0],
# [1,1,1]]
#
# Output:
# [[0,0,0],
# [0,1,0],
# [1,2,1]]
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Naive solution will be to iterate through all the cells using the two outer loops in the matrix and then check if its value is already 0, then shortest dist = 0
# and then if not, then we need to again iterate entirely from first cell to last cell using two inner nested loop to compute dist and update dist using follwoing  : 
# if current : (k, l) and our cell : (i, j) => dist = abs(k - i) + abs(l - j) 
# dist[i][j] = min(dist[i][j], abs(k - i) + abs(l - j))
# This will be TLE and will be 0(N^4) in worst case.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Can we do this better ?
# Yes, actually we can implement this using BFS and while computing start from all the nodes which has value equal to 0, we can keep updating the all distances 
# shortest for each cell because BFS gives shortest distance between two nodes.
# TIME : 0(ROWS * COLS), SPACE : 0(ROWS * COLS)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAN WE DO MORE BETTER THAN THIS ?
# YES, we can actually implement using DP as if we know shortest dist around the neighbours, then we can compute shortest in the current cell using min of all neighbours.
# in the first pass, we go from top to bottom filling of cells, then going from bottom to top filling of cells while updating all the distances using minimum.
# TIME : 0(ROWS * COLS), SPACE : 0(ROWS * COLS)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FIRST OPTIMIZED (BFS) :

import sys
from collections import deque 

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return matrix
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dist = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            
            curr = queue.popleft()
            for i in range(4):
                new_r, new_c = curr[0] + dirs[i][0], curr[1] + dirs[i][1]
                if new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols:
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        queue.append((new_r, new_c))
        
        return dist

# SECOND OPTIMIZED (DP) : 

import sys
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return matrix
        
        dist = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i < rows - 1:
                        dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                    if j < cols - 1:
                        dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        
        return dist
            
