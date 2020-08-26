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
# Naive solution would be to first do complete traversal of matrix, then set matrix[i][j] = 2, wherever in all the possible directions
# four adjacent directions : for [i, j] => [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]
# we have to check for all bounds, and if matrix[i][j] = 1, then matrix[i][j] = 2.
# Now, we go for second traversal, and similarly we keep going on until there is no change observed in the matrix (no more rotten oranges possible)
# Thus, we can simply run infinite while True loop, do complete traversal and check for all possible four directions if it's safe and if it's value is 1, set it 2
# and finally check if after the traversal, there is no change observed anywhere, then break otherwise keep doing it and increment a counter.
# Time : 0(MAx(R, C) * R * C), SPACE : 0(R * C)
# --------------------------------------------------------------------------------------------------------------------------
# Can we do better ?
# If we think carefully, then we can visalize this in terms of graph where each of the coordinates denotes nodes of the graph, and the rotten process at t = 0,
# indicates a first traversal, then at t = 1, all nodes at distance of 1 will be rotten (based on conditions), similary, at t = 2, all nodes at distance = 2 will be rotten
# and this process occcurs simulataneously for various points on the matrix.
# This type of traversal is similar to BFS and hence a queue will eb required for the traversal.
# It will be initialized with all the cells with value = 2 , so that in next traversal, all at a dist of 1, can be rotten, and so on....
# Now, queue structure will be saved as tuple (time, x-coordinate, y-coordinate) where time denotes current node's explored time, other values are simply the coordinates of current cell.
# TIME : 0(R * C), SPACE : 0(R * C)
# ---------------------------------------------------------------------------------------------------------------------------
# This can also be solved using Dynamic Programming which is discussed in DP.

from collections import deque

# check for bounds
def is_safe(mat, i, j, row, col):
    if i >= 0 and i <= row - 1 and j >= 0 and j <= col - 1:
        return True

    return False

# it will check the bounds and rot the oranges
def rot(queue, mat, time, i, j, row, col):

    if is_safe(mat, i, j, row, col):

        if is_safe(mat, i, j + 1, row, col) and mat[i][j + 1] == 1:
            mat[i][j + 1] = 2
            queue.append((time, i, j + 1))

        if is_safe(mat, i, j - 1, row, col) and mat[i][j - 1] == 1:
            mat[i][j - 1] = 2
            queue.append((time, i, j - 1))

        if is_safe(mat, i + 1, j, row, col) and mat[i + 1][j] == 1:
            mat[i + 1][j] = 2
            queue.append((time, i + 1, j))

        if is_safe(mat, i - 1, j, row, col) and mat[i - 1][j] == 1:
            mat[i - 1][j] = 2
            queue.append((time, i - 1, j))


# main function for BFS traversal
def compute_minimum_rot_time(mat):
    row, col = len(mat), len(mat[0])

    l = [(0, i, j) for i in range(row) for j in range(col) if mat[i][j] == 2]
    queue = deque(l)

    # to handle cases, trivial edge cases for length of 1 and value = 0
    if row == 1 and col == 1 and grid[0][0] == 0:
            return 0

    # to handle cases, trivial edge cases for length of 1 and value = 1
    if row == 1 and col == 1 and grid[0][0] == 1:
        return -1

    while queue:
        curr = queue.popleft()
        rot(queue, mat, curr[0] + 1, curr[1], curr[2], row, col)

    # check if there is any remaining "1" in the matrix, then it means it's not possible to rot all the oranges.
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                return -1

    return curr[0]

if __name__ == '__main__':
    assert compute_minimum_rot_time([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]) == 2
    assert compute_minimum_rot_time([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert compute_minimum_rot_time([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert compute_minimum_rot_time([[0,2]]) == 0
