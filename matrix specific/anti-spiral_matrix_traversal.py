# function to traverse the matrix in spiral anti-clockwise way
# logic is discussed in spiral one similar problem.
# k - starting row index
# m - ending row index
# l - starting column index
# n - ending column index
# i - iterator

def matrix_traversal(mat):
    m, n = len(mat), len(mat[0])
    if m == 0 and n == 0:
        return []

    k, l = 0, 0
    count = 0
    total = m * n
    # going over every element until one of the pointers exhaust
    while k < m and l < n:
        # printing first column

        if count == total:
            break

        for i in range(l, m, 1):
            print(mat[i][l], end = ", ")
            count += 1

        l += 1

        if count == total:
            break
        # printing last row

        for i in range(l, n):
            print(mat[m - 1][i], end = ", ")
            count += 1

        m -= 1

        if count == total:
            break
        # printing last column
        if k < m:
            for i in range(m - 1, k - 1, -1):
                print(mat[i][n - 1], end = ", ")
                count += 1

            n -= 1

        if count == total:
            break
        # printing first row
        if l < n:
            for i in range(n - 1, l - 1, -1):
                print(mat[k][i], end = ", ")
                count += 1

            k += 1

# driver function
if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
    mat1 = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_traversal(mat)
    print()
    matrix_traversal(mat1)
