# Program for computing (printing) sum of submatrices given as range of queries for a fixed matrix m * n where m = rows, n = columns
# and queries consists of four coordinates : (i, j, x, y) where (i, j) => top left corner , and (x, y) => right most bottom corner
# IDEA: logic is same as for overall sum computation -> idea of having preprocessed prefix sum array already stored as the matrix given will be fixed.
# and then for each query we can simply return the value using some formula in 0(1) 

# Time : 0(N^2) and Space : 0(N)

from sys import stdin, stdout


# function for computing prefix in 0(N^2)
def compute_prefix(mat):
    m, n = len(mat), len(mat[0])
    for i in range(0, m):
        for j in range(1, n):
            mat[i][j] += mat[i][j - 1]

    for i in range(1, m):
        for j in range(0, n):
            mat[i][j] += mat[i - 1][j]

    return mat

# # function for returning sum in 0(1)
def compute_sum(p, i, j, x, y):
    res = p[x][y]

    if i or j > 0:
        res = res + p[i - 1][j - 1] - p[i - 1][y] - p[x][j - 1]
    return res

def pretty_print(mat):
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

# driver function
if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 6], [5, 3, 8, 1, 2], [4, 6, 7, 5, 5], [2, 4, 8, 9, 4]]
    p = compute_prefix(mat)
    pretty_print(p)
    q = int(stdin.readline().strip())
    while q:
        i, j, x, y = list(map(int, stdin.readline().strip().split()))
        print(compute_sum(p, i, j, x, y))
        q -= 1
