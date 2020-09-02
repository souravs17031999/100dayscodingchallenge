# Program for counting all the unique paths possible from given source position to destination position in a 2-d grid.
# NOTE : We are only allowed to move right or down one at a time.
# We need to count all the possible paths which are unique like given below :
#
#    [S,->,  ->  ]
#    [| ,| ,->  |]
#    [| ,-> , E]
#
# Start from "S", we can see we have 3 unique paths possible to reach the end point "E".
# --------------------------------------------------------------------------------------------------------------------------
# We can observe that to reach E, we must also check which paths did we take intermediate that means at every point we have two possible choices,
# either go right , or go down and we have exhaust all the possiblites , hence first intuition for naive solution is recursion + backtracking.
# We will start from "S" and go for right and go for down and return the count of both choices.
# Base cases : if row and col are out of bound then return 0,
# if row == N-1 and col == N-1, then return 1, meaning we have found 1 path.
#
#
#                          (0, 0)
#                  /                 \
#               (1, 0)               (0, 1)
#               /   \            /         \
#        (2, 0)  (1, 1)     (1, 1)          (0, 2)
#            x     /\          /\            /    \
#            (2, 1) (2, 2)* (2, 1) (2, 2)* (1, 2)  x
#              x             x              /\
#                                      (2, 2)   x
#
# As, we can see (2, 2) E can be reached in 3 ways.
# Also, we observe that there overlapping subproblems.
# We can use DP to memoize it.

# METHOD 1: RECURSION
# -----------------------------------------------------------------------------------------------------------------------------

def count_grid(i, j, row, col):
    if i >= row or j >= col:
        return 0

    if i == row - 1 and j == col - 1:
        return 1

    return count_grid(i + 1, j, row, col) + count_grid(i, j + 1, row, col)




# METHOD 2 : DP MEMOIZED

cache = {}
def count_grid_recr(i, j, row, col):
    if i >= row or j >= col:
        return 0

    if i == row - 1 and j == col - 1:
        return 1

    if (i, j) in cache:
        return cache[(i, j)]


    cache[(i, j)] = count_grid_recr(i + 1, j, row, col) + count_grid_recr(i, j + 1, row, col)
    return cache[(i, j)]

# CAN WE DO MORE BETTER ?
# YES, WE CAN MAKE USE OF COMBINATORICS.
# Observation :- we can write all the combinations for the grid paths :
# for ex. [2 * 3]
# rows = 2, col = 3
# Now, total paths : RRD, DRR, RDR
# Then, we can observe that total right moves can be maximum (rows - 1), and then total downward moves can be maximum (col - 1).
# Hence, total possible moves/choices => rows + cols - 2 or m + n - 2
# Then, either we can choose 2 right moves or we can choose 2 downward moves, rest move is whatever left.
# so, total paths will be : (m + n - 2) C (n - 1)
# TIME : 0(N) or 0(M), space : 0(1)


if __name__ == '__main__':
    print(count_grid(0, 0, 3, 3))
    print(count_grid_recr(0, 0, 3, 3))
