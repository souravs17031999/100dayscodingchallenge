# Program for finding the perimeter of the island represented by the grid : row x col, where grid[i][j] = 1 means land, grid[i][j] = 0 means water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# One cell is a square with side length 1.
# Example 1:
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
#
# -------------
# | [0 1 0 0] |
# | [1 1 1 0] |   => - lines represent water all around the grid 
# | [0 1 0 0] |
# | [1 1 0 0] |
# -------------
#
# 
#
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:
#
# Input: grid = [[1]]
# Output: 4
# Example 3:
#
# Input: grid = [[1,0]]
# Output: 4
# -----------------------------------------------------------------------------------------------------------
# As can be seen from the above diagram, we can simply iterate over all the cells of matrix, and for every "1" having cell that is land, we can simply check for it's 
# all four sides : for curr pos (i, j) :
# up : i - 1, j
# down : i + 1, j
# left : i, j - 1
# right : i, j + 1
# and count up all those sides which have water in its surroundings, sum them up to get the perimeter of the island.
# like, in the above diagram, 
# 3 + 3 + 3 + 2 + 3 + 2 => 16 (sides having water in surroundings having "1" in cells in the shown grid)
# -----------------------------------------------------------------------------------------------------------
# TIME : 0(ROWS * COLS)

class Solution:
    def check_water_sides(self, grid, i, j, rows, cols):
        count = 0
        
        if i - 1 >= 0:
            if grid[i - 1][j] == 0:
                count += 1
        else:
            count += 1
        
        if i + 1 < rows:
            if grid[i + 1][j] == 0:
                count += 1
        else:
            count += 1
        
        if j - 1 >= 0:
            if grid[i][j - 1] == 0:
                count += 1
        else:
            count += 1
        
        if j + 1 < cols:
            if grid[i][j + 1] == 0:
                count += 1
        else:
            count += 1
        
        return count
        
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    perimeter += self.check_water_sides(grid, i, j, rows, cols)
        
        return perimeter
        
