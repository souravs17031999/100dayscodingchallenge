# Finding the number of islands through DFS approach.

class Solution:
    def dfs(self, mat, i, j):
        rows, cols = len(mat), len(mat[0])
        if i < 0 or j < 0 or i >= rows or j >= cols or mat[i][j] == '0':
            return 0

        mat[i][j] = '0'
        self.dfs(mat, i + 1, j)
        self.dfs(mat, i - 1, j)
        self.dfs(mat, i, j + 1)
        self.dfs(mat, i, j - 1)

        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid  == None or len(grid) == 0:
            return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num += self.dfs(grid, i, j)
        return num

if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1]]
    print(num_islands(mat, 5))
