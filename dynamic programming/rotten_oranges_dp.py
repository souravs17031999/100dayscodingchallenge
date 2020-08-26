# Program for computing minimum time for rotting all possible oranges kept in a matrix shaped basket.
# EX.
#
#      [2, 1, 0, 2, 1]
#      [1, 0, 1, 2, 1]
#      [1, 0, 0, 2, 1]
#
# ans = 3
# At time frame t0 = same as start
# now, at time frame t1 =
#
#      [2, 1, 0, 2, 1]
#      [1, 0, 1, 2, 1]
#      [1, 0, 0, 2, 1]
#
# At time frame t2 =
#
#      [2, 2, 0, 2, 2]
#      [2, 0, 2, 2, 2]
#      [2, 0, 0, 2, 2]
#
# Hence, all oranges are rotten.
# Note : it is also possible that not all oranges are rotten hence, in that case we need to return -1.
# -------------------------------------------------------------------------------------------------------------------------
# We have already seen other methods, here we use top down DP approach as there are various overlapping subproblems which can be cached.

import sys


def distance(dp, mat, i, j, row, col, visited):

    if i >= 0 and i <= row and j >= 0 and j <= col:
        return sys.maxsize

    elif dp[i][j] > 0 and dp[i][j] < sys.maxsize:
        return dp[i][j]

    elif dp[i][j] == 0:
        dp[i][j] = sys.maxsize
        return sys.maxsize

    elif dp[i][j] == 2:
        dp[i][j] = 0
        return 0

    elif visited[i][j]:
        return sys.maxsize

    else:
        visited[i][j] = 1

        up = distance(dp, mat, i - 1, j, row, col, visited)
        down = distance(dp, mat, i + 1, j, row, col, visited)
        left = distance(dp, mat, i, j - 1, row, col, visited)
        right = distance(dp, mat, i, j + 1, row, col, visited)

        dp[i][j] = 1 + min(up, down, left, right)
        visited[i][j] = 0

    return dp[i][j]


def compute_minimum_rot_time(mat):
    row, col = len(mat), len(mat[0])

    dp = [[0 for i in range(col)] for _ in range(row)]
    visited = [[0 for i in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                distance(dp, mat, i, j, row, col, visited)

    time = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1 and dp[i][j] > time:
                time = max(time, dp[i][j])

    if time < sys.maxsize:
        return time
    else:
        return -1


if __name__ == '__main__':
    assert compute_minimum_rot_time([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]) == 2
    assert compute_minimum_rot_time([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert compute_minimum_rot_time([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert compute_minimum_rot_time([[0,2]]) == 0
