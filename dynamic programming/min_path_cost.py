# The program wants to compute the minimum cost to reach bottom right corner from top left corner for a given grid
# which has some cost associated with every cell (i, j) where movement is restricted to only downwards and rightwards.
# ------------------------------------------------------------------------------------------------------------------------
# We could possibly first think of greedy approach due to its optimization nature, but it gives wrong results !
# So, let's discuss about this in detail.
#
#
#            [1 3 5 8]
#            [4 2 1 7]
#            [4 3 2 3]
# -------------------------------------------------------------------------------------------------------
# If we start from (0, 0) and want to move to (2, 3).
# There are two choices at every cell point either right or down.
#                   (0, 0)
#                    /  \
#                (1, 0)  (0, 1)
#                /   \      /  \
#           (2, 0) (1, 1) (1, 1) (0, 2)
#              \
#             (2, 1)
#
# Now, this recursion tree shows overlapping sub problems and hence, we need to memoize it.
# Then, we can apply DP bottom up tabulation.
# ----------------------------------------------------------------------------------------------------------
# TIME : 0(N^2), SPACE : 0(N^2)

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m == 0 and n == 0:
        return 0
    if m == 1 and n == 1:
        return grid[0][0]

    dp = [[None for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]

    for col in range(1, n):
        dp[0][col] = dp[0][col - 1] + grid[0][col]

    for row in range(1, m):
        dp[row][0] = dp[row - 1][0] + grid[row][0]

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

    return dp[m-1][n-1]

if __name__ == '__main__':
    #print(minPathSum([[1,3,1], [1,5,1], [4,2,1]]))
    print(minPathSum([[1,2,5],[3,2,1]]))
