# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#
# Return the number of negative numbers in grid.
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
#
# Input: grid = [[-1]]
# Output: 1

# ---------------------------------------------------------------------------------------------
# Naive solution would be to loop around the matrix using two loops in 0(M * N), M AND N ARE DIMENSIONS
# OF MATRIX (GRID) AND ignore the sorted property.
# But we can do better than this using binary search in inner loop, in 0(M * LOG(N))
# More elegant and efficient solution will be start at one of the corners of the matrix and then
# using sorted property, we can move our both row and col pointers and count if current is -ve.
# TIME : 0(N + M)
# ---------------------------------------------------------------------------------------------
# Trick is in only to choose the correct corners.
# If like below given in decreasing order (non-increasing order) : start from left bottom most corner
# If increasing order : start from top right most corner.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        nrows, ncols = len(grid), len(grid[0])

        if not nrows and not ncols:
            return 0

        i, j = nrows-1, 0
        count = 0
        while i >= 0 and j < ncols:
            if grid[i][j] < 0:
                count += (ncols - j)
                i -= 1
            else:
                j += 1

        return count

grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
print(countNegatives(grid))
